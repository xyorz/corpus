import sys, os, lucene, time, re, json
from java.nio.file import Paths
from org.apache.lucene.store import SimpleFSDirectory, FSDirectory, Directory
from org.apache.lucene.search import IndexSearcher, BooleanQuery, BooleanClause, TermQuery
from org.apache.lucene.search.spans import SpanQuery, SpanNearQuery, SpanTermQuery
from org.apache.lucene.index import DirectoryReader, Term
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.analysis.core import KeywordAnalyzer
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from CorpusCommandParser import CommandParser
from function.operation.Content import get_detail, add_tag


class Searcher(object):
    def __init__(self, commandInfo: CommandParser, directory: str):
        d = SimpleFSDirectory(Paths.get(directory))
        self._search = IndexSearcher(DirectoryReader.open(d))
        self._commandInfo = commandInfo
        self._doc = {}
        self._resultSentencesList = []

    def search(self, field: str):
        sear = self._search
        if len(self._commandInfo.getKey()) == 0 or self._commandInfo.getKey()[0] in ['-', '~']:
            query = QueryParser(field, StandardAnalyzer()).parse(make_parser(self._commandInfo.getWordList()[0]))
        elif self._commandInfo.getKey()[0] == '#':
            query1 = QueryParser(field, StandardAnalyzer()).parse(make_parser(self._commandInfo.getWordList()[0]))
            query2 = QueryParser(field, StandardAnalyzer()).parse(make_parser(self._commandInfo.getWordList()[1]))
            bc1 = BooleanClause(query1, BooleanClause.Occur.MUST)
            bc2 = BooleanClause(query2, BooleanClause.Occur.MUST)
            query = BooleanQuery.Builder().add(bc1).add(bc2).build()
        elif self._commandInfo.getKey()[0] in ['$', '+']:
            bq = BooleanQuery.Builder()
            for w in self._commandInfo.getWordList():
                queryx = QueryParser(field, StandardAnalyzer()).parse(make_parser(w))
                bc = BooleanClause(queryx, BooleanClause.Occur.MUST)
                bq.add(bc)
            query = bq.build()
        else:
            query = ''
        hits = sear.search(query, 999999)
        for hit in hits.scoreDocs:
            doc = sear.doc(hit.doc)
            res = doc.get(field)
            id = doc.get(field+'_id')
            if doc_hit(res, self._commandInfo):
                sentences = re.split('[!?！？。]', res)
                map(lambda x: sentences.pop(x) if x == '' else 0, range(len(sentences)))
                for sentence in sentences:
                    if key_filter(self._commandInfo, sentence):
                        self._doc[id] = res
                        self._resultSentencesList.append((id, sentence))
        return self

    def ancientSearch(self, field):
        sear = self._search
        fieldOnly = False
        # 只搜索域
        if len(self._commandInfo.getWordList()) == 0:
            fieldOnly = True
            bq = BooleanQuery.Builder()
            fields = self._commandInfo.getFields()
            for key in fields:
                queryx = QueryParser(key, KeywordAnalyzer()).parse(fields[key][0])
                bc = BooleanClause(queryx, BooleanClause.Occur.MUST)
                bq.add(bc)
            query = bq.build()

        elif len(self._commandInfo.getKey()) == 0 or self._commandInfo.getKey()[0] in ['-', '~']:
            bq = BooleanQuery.Builder()
            q = QueryParser(field, StandardAnalyzer()).parse(make_parser(self._commandInfo.getWordList()[0]))
            bc = BooleanClause(q, BooleanClause.Occur.MUST)
            bq.add(bc)
            for i in self._commandInfo.getFields():
                if i == 'section' or i == 'document':
                    continue
                queryx = QueryParser(i, KeywordAnalyzer()).parse(make_ancient_parser(self._commandInfo.getFields()[i]))
                bc = BooleanClause(queryx, BooleanClause.Occur.MUST)
                bq.add(bc)
            query = bq.build()
        elif self._commandInfo.getKey()[0] == '#':
            bq = BooleanQuery.Builder()
            query1 = QueryParser(field, StandardAnalyzer()).parse(make_parser(self._commandInfo.getWordList()[0]))
            query2 = QueryParser(field, StandardAnalyzer()).parse(make_parser(self._commandInfo.getWordList()[1]))
            bc1 = BooleanClause(query1, BooleanClause.Occur.MUST)
            bc2 = BooleanClause(query2, BooleanClause.Occur.MUST)
            bq.add(bc1).add(bc2)
            for i in self._commandInfo.getFields():
                if i == 'section' or i == 'document':
                    continue
                queryx = QueryParser(i, KeywordAnalyzer()).parse(make_ancient_parser(self._commandInfo.getFields()[i]))
                bc = BooleanClause(queryx, BooleanClause.Occur.MUST)
                bq.add(bc)
            query = bq.build()
        elif self._commandInfo.getKey()[0] in ['$', '+']:
            bq = BooleanQuery.Builder()
            for w in self._commandInfo.getWordList():
                queryx = QueryParser(field, StandardAnalyzer()).parse(make_parser(w))
                bc = BooleanClause(queryx, BooleanClause.Occur.MUST)
                bq.add(bc)
            for i in self._commandInfo.getFields():
                if i == 'section' or i == 'document':
                    continue
                queryx = QueryParser(i, KeywordAnalyzer()).parse(make_ancient_parser(self._commandInfo.getFields()[i]))
                bc = BooleanClause(queryx, BooleanClause.Occur.MUST)
                bq.add(bc)
            query = bq.build()
        else:
            query = ''
        hits = sear.search(query, 9999)
        for hit in hits.scoreDocs:
            doc = sear.doc(hit.doc)
            res = doc.get(field)
            id = doc.get('id')
            detail = get_detail(doc)
            zhujie = detail['zhujie']
            if detail['detail'] and 'detail' in detail['detail'].keys():
                detail['detail'] = detail['detail']['detail']
            detail.pop('zhujie')
            detail.pop('text')
            detail.pop('type')
            detail = json.dumps(detail)
            if fieldOnly:
                if not doc.get("text").strip():
                    continue
                if id.count(".") == 2:
                    self._doc[id] = doc.get("text")
                    self._resultSentencesList.append((id, doc.get("text")))
                elif id.count(".") == 1:
                    searcher = self._search
                    query = QueryParser('id', KeywordAnalyzer()).parse(id + '.1')
                    hits = searcher.search(query, 1)

                    for hit in hits.scoreDocs:
                        doc = searcher.doc(hit.doc)
                        res = doc.get("text")
                        if res:
                            self._doc[id+".1"] = doc.get('text')
                            self._resultSentencesList.append((id + ".1", doc.get('text')))
                else:
                    searcher = self._search
                    query = QueryParser('id', KeywordAnalyzer()).parse(id + '.1.1')
                    hits = searcher.search(query, 1)
                    for hit in hits.scoreDocs:
                        doc = searcher.doc(hit.doc)
                        res = doc.get("text")
                        if not doc.get("text").strip():
                            continue
                        if res:
                            self._doc[id+".1.1"] = doc.get('text')
                            self._resultSentencesList.append((id + ".1.1", doc.get('text')))
            elif doc_hit(res, self._commandInfo):
                if key_filter(self._commandInfo, res):
                    if 'section' in self._commandInfo.getFields().keys():
                        if not search_upper_title_filter(id, sear, self._commandInfo.getFields()['section'], 0):
                            continue
                    if 'document' in self._commandInfo.getFields().keys():
                        if not search_upper_title_filter(id, sear, self._commandInfo.getFields()['document'], 1):
                            continue
                    self._doc[id] = res
                    self._resultSentencesList.append((id, res, detail, zhujie))
        return self

    def getResult(self, left: int, right: int):
        result_list = []
        for r in self._resultSentencesList:

            doc = self._doc[r[0]]
            s_position = doc.find(r[1])

            # 只搜索域，无关键词
            if len(self._commandInfo.getWordList()) == 0:
                if len(doc) >= left + right:
                    end = s_position + left + right
                else:
                    end = s_position + len(doc)
                result_list.append({'left': '', 'right': doc[s_position: end], 'mid': '', 'id': r[0], 'beg': s_position, 'end': s_position + len(r[1])})
                continue

            # 关键词位置居中
            if not self._commandInfo.getImpWord() and len(self._commandInfo.getWordList()) > 0:
                imp_word = SectionPosition(self._commandInfo, r[1]).getKeyWord()
            else:
                if r[1].find(self._commandInfo.getImpWord()) >= 0:
                    imp_word = self._commandInfo.getImpWord()
                else:
                    imp_word = SectionPosition(self._commandInfo, r[1]).getKeyWord()
            mid_beg = s_position + r[1].find(imp_word)
            mid_end = mid_beg + len(imp_word) + 1
            s_m = doc[mid_beg:mid_end-1]
            if mid_beg - left >= 0:
                s_l = doc[mid_beg-left:mid_beg]
            else:
                s_l = doc[0:mid_beg]
            if mid_beg + right <= len(doc):
                s_r = doc[mid_end-1:mid_end+right]
            else:
                s_r = doc[mid_end-1:len(doc)]
            s_beg = s_position
            s_end = s_beg + len(r[1]) + 1
            result_list.append({'left': s_l, 'right': s_r, 'mid': s_m, 'id': r[0], 'beg': s_beg, 'end': s_end, 'detail': r[2], 'zhujie': r[3]})
        return result_list


def make_parser(list):
    res = '('
    for words in list:
        for word in words:
            res += '('
            for w in word:
                res += w + ' AND '
            res = res[0: -4]
            res = res + ')'
            res += ' OR '
        res = res[:len(res)-4]
        res += ') AND ('
    res = res[:len(res)-6]
    return res


def make_ancient_parser(list):
    res = ''
    for words in list:
        res += words + ' OR '
    return res[0:-4]


def search_upper_title_filter(id: str, seacher: IndexSearcher, titleFields: list, type: int):
    sear = seacher
    if type == 0:
        upper_id = id[0:id.rfind('.')]
    else:
        upper_id = id[0:id.find('.')]
    query = QueryParser('id', KeywordAnalyzer()).parse(upper_id)
    hits = sear.search(query, 1)
    res = ''
    for hit in hits.scoreDocs:
        doc = sear.doc(hit.doc)
        if type == 0:
            res = doc.get('section')
        else:
            res = doc.get('document')
    if res in titleFields:
        return True
    return False


def doc_hit(doc: str, commandInfo: CommandParser):
    m = 0
    for i in commandInfo.getWordList():
        m += 1
        for j in i:
            j_list = []
            for k in j:
                t = doc.find(k)
                if t >= 0:
                    j_list.append(t)
            if not commandInfo.getKey():
                if len(j_list) == 0:
                    return False
            elif commandInfo.getKey()[0] in ['-', '~'] and m == 1:
                if len(j_list) == 0:
                    return False
            elif commandInfo.getKey()[0] not in ['-', '~']:
                if len(j_list) == 0:
                    return False

    return True


class SectionPosition(object):
    def __init__(self, commandInfo: CommandParser, sentence: str):
        self._commandInfo = commandInfo
        self._sentence = sentence
        self._section = []
        self._search_key_word = ''

    def build(self):
        m = 0
        for i in self._commandInfo.getWordList():
            m += 1
            tupList = []
            for j in i:
                tup = []
                for k in j:
                    temp = self._sentence.find(k)
                    if temp >= 0:
                        tup.append((temp, temp+len(k)))
                if not self._commandInfo.getKey():
                    if len(tup) == 0:
                        return
                elif self._commandInfo.getKey()[0] in ['-', '~'] and m == 1:
                    if len(tup) == 0:
                        return
                elif self._commandInfo.getKey()[0] not in ['-', '~']:
                    if len(tup) == 0:
                        return
                tupList.append(tup)
            res_tup = []
            for l in tupList:
                t_min = float('inf')
                t_min_r = 0
                t_r = float('inf')
                for t in l:
                    if t[0] < t_min:
                        t_min = t[0]
                        t_min_r = t[1]
                    if t[1] < t_r:
                        t_r = t[1]
                if t_r < t_min_r:
                    res_tup.append((t_min, t_min_r))
                else:
                    res_tup.append((t_min, t_r))
            begList = []
            endList = []
            for j in res_tup:
                begList.append(j[0])
                endList.append(j[1])
            self._section.append((min(begList), max(endList)))
        return self

    def getSection(self):
        return self._section

    def getKeyWord(self):
        m = float('inf')
        m_r = 0
        for i in self._commandInfo.getWordList():
            for j in i:
                for k in j:
                    p = self._sentence.find(k)
                    if 0 <= p < m:
                        m = p
                        m_r = p + len(k)
        return self._sentence[m:m_r]


def key_filter(commandInfo: CommandParser, sentence: str):
    t = SectionPosition(commandInfo, sentence).build()
    if t:
        sp = t.getSection()
    else:
        return False
    if not commandInfo.getKey():
        return True
    if commandInfo.getKey()[0] in ['$', '+']:
        for i in range(len(sp)):
            if not i+1 <= len(sp)-1:
                return True
            elif commandInfo.getKey()[i] == '$':
                if 0 > sp[i+1][0] - sp[i][1] or sp[i+1][0] - sp[i][1] > int(commandInfo.getNum()[i]):
                    return False
            elif commandInfo.getKey()[i] == '+':
                if sp[i+1][0] - sp[i][1] != int(commandInfo.getNum()[i]):
                    return False
    elif commandInfo.getKey()[0] == '#':
        if abs(sp[0][1] - sp[1][0]) > int(commandInfo.getNum()[0]) and abs(sp[0][0] - sp[1][1]) > int(commandInfo.getNum()[0]):
            return False
        return True
    elif commandInfo.getKey()[0] in ['-', '~']:
        if commandInfo.getKey()[0] == '-':
            if sp[1][0] - sp[0][1] < int(commandInfo.getNum()[0]) or sp[0][0] - sp[1][1] > 0:
                return False
        elif commandInfo.getKey()[0] == '~':
            if sp[0][0] - sp[1][1] < int(commandInfo.getNum()[0]) or sp[1][0] - sp[0][1] > 0:
                return False
        return True