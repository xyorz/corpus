import sys, os, lucene, time, re, json
from java.nio.file import Paths
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.search import IndexSearcher, BooleanQuery, BooleanClause, TermQuery, RegexpQuery
from org.apache.lucene.search.spans import SpanQuery, SpanNearQuery, SpanTermQuery, SpanOrQuery, SpanMultiTermQueryWrapper, SpanNotQuery
from org.apache.lucene.index import DirectoryReader, Term
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__ + '../../')))
from NewPatternCommandParser import CommandParser
from Content import new_get_content, get_text_from_content


word_reg = "[\u4E00-\u9FA5\uF900-\uFA2D]"
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
        self._cur_field = None
        self._res = None
        self._reg = None

    def search(self, field):
        s = self._search
        u = self._userQuery
        zh_to_hant_dict = self._zh_to_hant_dict
        info = u.getFlagsInfo()
        flags_list = u.getFlagsList()
        sq_list = []
        word_index_list = []
        index_count = 0
        for flag in flags_list:
            if flag["type"] == "word":
                word_index_list.append(index_count)
                if len(flag["content"]) == 1:
                    if flag["content"][0] in zh_to_hant_dict:
                        stq_list = [SpanTermQuery(Term(field, flag["content"][0]))]
                        for hant in zh_to_hant_dict[flag["content"][0]]:
                            stq_list.append(SpanTermQuery(Term(field, hant)))
                        sq_list.append(SpanOrQuery(stq_list))
                    else:
                        sq_list.append(SpanTermQuery(Term(field, flag["content"][0])))
                else:
                    snq_list = []
                    for w in flag["content"]:
                        if w in zh_to_hant_dict:
                            stq_list = [SpanTermQuery(Term(field, w))]
                            for hant in zh_to_hant_dict[w]:
                                stq_list.append(SpanTermQuery(Term(field, hant)))
                            snq_list.append(SpanOrQuery(stq_list))
                        else:
                            snq_list.append(SpanTermQuery(Term(field, w)))
                    sq_list.append(SpanNearQuery(snq_list, 0, True))
            else:
                sq_list.append({"op": info[flag["content"]]["op"], "num": info[flag["content"]]["num"]})
            index_count += 1
        q = None
        count = 0
        for index in word_index_list:
            if count == 0:
                q = sq_list[index]
                count += 1
            else:
                if not isinstance(sq_list[index-1], dict):
                    q = SpanNearQuery([q, sq_list[index]], 0, True)
                else:
                    q = SpanNearQuery([q, sq_list[index]], sq_list[index-1]["num"][-1], True)
        query = q
        # 过滤项
        filters = u.getFields()
        bq = BooleanQuery.Builder()
        bq.add(BooleanClause(query, BooleanClause.Occur.MUST))
        for key in filters.keys():
            cur_reg = '('
            for ft in filters[key]:
                cur_reg += ft + '|'
            cur_reg = cur_reg[0: -1] + ')'
            rq = RegexpQuery(Term(key, cur_reg))
            bq.add(BooleanClause(rq, BooleanClause.Occur.MUST))
        query = bq.build()
        top_docs = s.search(query, 9999)
        self._cur_field = field

        reg = get_test_reg(flags_list, info, zh_to_hant_dict)
        doc_id_list = []
        hits = top_docs.scoreDocs
        for hit in hits:
            doc = s.doc(hit.doc)
            text = doc.get("text")
            match_res = re.search(reg, text)
            if match_res:
                doc_id_list.append(hit.doc)
        self._res = doc_id_list
        self._reg = reg
        return self

    def get_by_page(self, page_num=0, page_size=30, length_tup=(30, 30)):
        doc_id_list = self._res
        s = self._search
        d = self._dir
        reg = self._reg
        doc_list = []
        total_hits = len(doc_id_list)
        # 分页
        start_index = page_num * page_size
        if start_index + page_size <= len(doc_id_list):
            end_index = start_index + page_size
        else:
            end_index = len(doc_id_list)
        for i in range(start_index, end_index):
            doc = s.doc(doc_id_list[i])
            cur_id = doc.get("id")
            r = doc.get("text")
            document = doc.get("document")
            section = doc.get("section")
            match_span = re.search(reg, r).span()
            context = get_text_from_content(new_get_content(d, cur_id))
            prev_len = len(context["prev"][-1])
            str_context = context["prev"][-1] + context["cur"][0] + context["next"][0]
            match_span = (prev_len + match_span[0], prev_len + match_span[1])
            mid = str_context[match_span[0]: match_span[1]]
            if match_span[0] < length_tup[0]:
                left = str_context[0: match_span[0]]
            else:
                left = str_context[match_span[0] - length_tup[0]: match_span[0]]
            if len(str_context) - match_span[1] < length_tup[1]:
                right = str_context[match_span[1]:]
            else:
                right = str_context[match_span[1]: match_span[1] + length_tup[1]]
            doc_list.append({"left": left, "mid": mid, "right": right, "id": cur_id, "document": document, "section": section})
        return {"total": total_hits, "doc_list": doc_list, "regexps": [reg]}

    def get_result_statistics_by_keyword(self):
        doc_ids = self._res
        # print(doc_ids)
        s = self._search
        reg = self._reg
        res_dict = {}
        for doc_id in doc_ids:
            doc = s.doc(doc_id)
            text = doc.get("text")
            key_word = re.search(reg, text).group()
            if key_word:
                if key_word in res_dict.keys():
                    res_dict[key_word] += 1
                else:
                    res_dict[key_word] = 1
        return res_dict

    def get_result_statistics_by_field(self, field):
        doc_ids = self._res
        s = self._search
        res_dict = {}
        for doc_id in doc_ids:
            doc = s.doc(doc_id)
            field_val = doc.get(field)
            if field_val:
                if field_val in res_dict.keys():
                    res_dict[field_val] += 1
                else:
                    res_dict[field_val] = 1
        return res_dict


def get_test_reg(flags_list, flags_info, zh_to_hant_dict):
    reg = ""
    mem = []
    for flag in flags_list:
        if flag["type"] == "word":
            word_hant_reg = ""
            w_hant_reg = ""
            for w in flag["content"]:
                w_hant_reg += "[" + w
                if w in zh_to_hant_dict:
                    for hant in zh_to_hant_dict[w]:
                        w_hant_reg += hant
                w_hant_reg += "]"
            word_hant_reg += w_hant_reg
            reg += word_hant_reg
        else:
            f_info = flags_info[flag["content"]]
            op = f_info["op"]
            num = f_info["num"]
            if flag["content"] not in mem:
                mem.append(flag["content"])
                if op == "<":
                    reg += "(" + word_reg + "{1," + str(num[0]) + "})"
                elif op == "-":
                    reg += "(" + word_reg + "{" + str(num[0]) + "," + str(num[1]) + "})"
                else:
                    reg += "(" + word_reg + "{" + str(num[0]) + "})"
            else:
                reg += "\\" + str(mem.index(flag["content"]) + 1)
    return reg


def initVM():
    vm_env = lucene.getVMEnv()
    if vm_env:
        vm_env.attachCurrentThread()
    else:
        lucene.initVM(vmargs=['-Djava.awt.headless=true'])


if __name__ == '__main__':
    # uc = "(V=1)先儒(K<5)釋不"
    initVM()
    # uc = "基立而後可大成也"
    uc = "好"
    st = time.time()
    ucp = CommandParser(uc)
    print(Searcher(ucp, index_dir).search('text').get_result_statistics_by_field("dynasty"))
    et = time.time()
    print('const:' + str(et - st))
