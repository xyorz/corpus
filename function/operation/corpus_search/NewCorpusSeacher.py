import sys, os, lucene, time, re, json
from java.nio.file import Paths
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.search import IndexSearcher, BooleanQuery, BooleanClause, TermQuery, RegexpQuery
from org.apache.lucene.search.spans import SpanQuery, SpanNearQuery, SpanTermQuery, SpanOrQuery, SpanMultiTermQueryWrapper, SpanNotQuery
from org.apache.lucene.index import DirectoryReader, Term
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__ + '../../')))
from CorpusCommandParser import CommandParser
from Content import new_get_content, get_text_from_content

index_dir = "../../index/index_ancient"
index_dir_server = "./function/index/index_ancient"


class Searcher(object):
    def __init__(self, userQuery: str, directory: str, zh_to_hant_dict=None):
        d = SimpleFSDirectory(Paths.get(directory))
        if zh_to_hant_dict:
            self._zh_to_hant_dict = zh_to_hant_dict
        else:
            self._zh_to_hant_dict = {}
        self._dir = directory
        self._search = IndexSearcher(DirectoryReader.open(d))
        self._userQuery = CommandParser(userQuery)
        self._res = None
        self._cur_field = None

    def search(self, field):
        s = self._search
        u = self._userQuery
        z = self._zh_to_hant_dict
        keys = u.getKey()
        nums = u.getNum()
        word_list = u.getWordList()
        filters = u.getFields()
        # 只检索过滤项
        if len(word_list) == 0:
            query = None
        # 简单项
        elif len(keys) == 0:
            query = simple_term_to_query(field, word_list[0], z)
        elif keys[0] == '#':
            query_left = simple_term_to_query(field, word_list[0], z)
            query_right = simple_term_to_query(field, word_list[1], z)
            query = SpanNearQuery([query_left, query_right], int(nums[0]), False)
        elif keys[0] == '+' or keys[0] == '$':
            prev_query = simple_term_to_query(field, word_list[0], z)
            for i in range(len(keys)):
                cur_query = simple_term_to_query(field, word_list[i + 1], z)
                if keys[i] == '+':
                    span_list = [prev_query]
                    for j in range(int(nums[i])):
                        span = SpanMultiTermQueryWrapper(RegexpQuery(Term(field, '.')))
                        span_list.append(span)
                    span_list.append(cur_query)
                    prev_query = SpanNearQuery(span_list, 0, True)
                else:
                    span_list = [prev_query, cur_query]
                    prev_query = SpanNearQuery(span_list, int(nums[i]), True)
            query = prev_query
        elif keys[0] == '-' or keys[0] == '~':
            query_left = simple_term_to_query(field, word_list[0], z)
            query_right = simple_term_to_query(field, word_list[1], z)
            if keys[0] == '-':
                n_q_list = [query_left, query_right]
            else:
                n_q_list = [query_right, query_left]
            n_query = SpanNearQuery(n_q_list, int(nums[0])-1, True)
            bq = BooleanQuery.Builder()
            bc1 = BooleanClause(query_left, BooleanClause.Occur.MUST)
            bc2 = BooleanClause(n_query, BooleanClause.Occur.MUST_NOT)
            query = bq.add(bc1).add(bc2).build()
        else:
            raise ValueError("检索语句错误！")
        # 过滤项
        bq = BooleanQuery.Builder()
        if query:
            bq.add(BooleanClause(query, BooleanClause.Occur.MUST))
        for key in filters.keys():
            cur_reg = '('
            for ft in filters[key]:
                cur_reg += ft + '|'
            cur_reg = cur_reg[0: -1] + ')'
            rq = RegexpQuery(Term(key, cur_reg))
            bq.add(BooleanClause(rq, BooleanClause.Occur.MUST))
        query = bq.build()
        self._res = s.search(query, 100000)
        self._cur_field = field
        return self

    def get_by_page(self, page_num=0, page_size=30, length_tup=(30, 30), use_context=True):
        top_docs = self._res
        s = self._search
        f = self._cur_field
        d = self._dir
        zh_to_hant_dict = self._zh_to_hant_dict
        # 用户指定的居中关键词
        imp_word = self._userQuery.getImpWord()
        # 用户检索语句中的所有关键词
        key_word_list = self._userQuery.getKeyWordList()
        # 关键字简繁处理
        key_word_list = key_word_list_add_hant(zh_to_hant_dict, key_word_list)
        doc_list = []
        total_hits = top_docs.totalHits
        hits = top_docs.scoreDocs
        start_index = page_num * page_size
        if start_index + page_size <= len(hits):
            end_index = start_index + page_size
        else:
            end_index = len(hits)
        for i in range(start_index, end_index):
            doc = s.doc(hits[i].doc)
            if not doc:
                break
            r = doc.get(f)
            cur_id = doc.get("id")
            document = doc.get("document")
            section = doc.get("section")
            # 寻找检索项关键词位置
            mid_pos = None
            if imp_word:
                imp_word_reg = ""
                for w in imp_word:
                    imp_word_reg += "[" + w
                    if w in zh_to_hant_dict:
                        for w_hant in zh_to_hant_dict[w]:
                            imp_word_reg += w_hant
                    imp_word_reg += "]"
                mid_pos = re.search(imp_word_reg, r)
                if mid_pos:
                    mid_pos = mid_pos.span()
                # mid_index = r.find(imp_word)
                # if mid_index >= 0:
                #     mid_pos = [mid_index, mid_index + len(imp_word)]
            if not mid_pos:
                for word in key_word_list:
                    mid_index = r.find(word)
                    if mid_index >= 0:
                        mid_pos = [mid_index, mid_index + len(word)]
                        break
            if not mid_pos:
                mid_pos = [0, 0]
            if use_context:
                context = get_text_from_content(new_get_content(d, cur_id))
            else:
                context = {"prev": [r[0: mid_pos[0]]], "cur": [r[mid_pos[0]: mid_pos[1]]], "next": [r[mid_pos[1]:]]}
            prev_len = len(context["prev"][-1])
            str_context = context["prev"][-1] + context["cur"][0] + context["next"][0]
            mid_pos = (prev_len + mid_pos[0], prev_len + mid_pos[1])
            mid = str_context[mid_pos[0]: mid_pos[1]]
            if mid_pos[0] < length_tup[0]:
                left = str_context[0: mid_pos[0]]
            else:
                left = str_context[mid_pos[0]-length_tup[0]: mid_pos[0]]
            if len(str_context) - mid_pos[1] < length_tup[1]:
                right = str_context[mid_pos[1]:]
            else:
                right = str_context[mid_pos[1]: mid_pos[1]+length_tup[1]]
            doc_list.append({"left": left, "mid": mid, "right": right, "id": cur_id, "document": document, "section": section})
        return {"total": total_hits, "doc_list": doc_list, "keywords": key_word_list}

    def get_result_statistics_by_keyword(self):
        s = self._search
        top_docs = self._res
        zh_to_hant_dict = self._zh_to_hant_dict
        key_word_list = self._userQuery.getKeyWordList()
        key_word_list = key_word_list_add_hant(zh_to_hant_dict, key_word_list)
        res_dict = {}
        hits = top_docs.scoreDocs
        for hit in hits:
            doc = s.doc(hit.doc)
            text = doc.get("text")
            for word in key_word_list:
                if text.find(word) >= 0:
                    if word in res_dict.keys():
                        res_dict[word] += 1
                    else:
                        res_dict[word] = 1
        return res_dict

    def get_result_statistics_by_field(self, field):
        s = self._search
        top_docs = self._res
        res_dict = {}
        hits = top_docs.scoreDocs
        for hit in hits:
            doc = s.doc(hit.doc)
            field_val = doc.get(field)
            if field_val:
                if field_val in res_dict.keys():
                    res_dict[field_val] += 1
                else:
                    res_dict[field_val] = 1
        return res_dict


# 简单项转换为spanQuery
def simple_term_to_query(field, word_list, zh_to_hant_dict=None):
    if not zh_to_hant_dict:
        zh_to_hant_dict = {}
    soq_list = []
    for words in word_list:
        snq_list = []
        for word in words:
            snq = SpanNearQuery.Builder(field, True)
            snq.setSlop(0)
            if len(word) == 1:
                if word[0] in zh_to_hant_dict:
                    stq_list = [SpanTermQuery(Term(field, word[0]))]
                    for hant in zh_to_hant_dict[word[0]]:
                        stq_list.append(SpanTermQuery(Term(field, hant)))
                    snq_list.append(SpanOrQuery(stq_list))
                else:
                    snq_list.append(SpanTermQuery(Term(field, word[0])))
            else:
                for w in word:
                    if w in zh_to_hant_dict:
                        stq_list = [SpanTermQuery(Term(field, w))]
                        for hant in zh_to_hant_dict[w]:
                            stq_list.append(SpanTermQuery(Term(field, hant)))
                        snq.addClause(SpanOrQuery(stq_list))
                    else:
                        snq.addClause(SpanTermQuery(Term(field, w)))
                snq_list.append(snq.build())
        soq = SpanOrQuery(snq_list)
        soq_list.append(soq)
    if len(soq_list) == 1:
        return soq_list[0]
    return SpanNearQuery(soq_list, 999, False)


def key_word_list_add_hant(zh_to_hant_dict, key_word_list):
    for word in key_word_list:
        for w in word:
            if w in zh_to_hant_dict:
                for hant in zh_to_hant_dict[w]:
                    key_word_list.append(word.replace(w, hant))
    return key_word_list


# def find_mid_pos(content, keys, nums)


def initVM():
    vm_env = lucene.getVMEnv()
    if vm_env:
        vm_env.attachCurrentThread()
    else:
        lucene.initVM(vmargs=['-Djava.awt.headless=true'])


if __name__ == '__main__':
    # uc = "復凡人#0皆必先習 每三過自視"
    # uc = "论語義疏"
    # uc = "豈可不經-3妄傳之乎"
    # uc = "妄傳之乎~4豈可不經"
    uc = "能致|吾|我"
    initVM()
    # uc = "基立而後可大成也"
    st = time.time()
    ucp = CommandParser(uc)
    print(Searcher(ucp, index_dir).search('text').get_result_statistics_by_field("author"))
    et = time.time()
    print('const:' + str(et - st))
