import sys, os, lucene, time, re, json
from java.nio.file import Paths
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.search import IndexSearcher, BooleanQuery, BooleanClause, TermQuery
from org.apache.lucene.index import DirectoryReader, Term
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.analysis.core import KeywordAnalyzer
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from PatternCommandParser import CommandParser
from function.operation.Content import get_detail, add_tag


class PatternSearcher(object):
    def __init__(self, searchWord: str, indexDir: str):
        commandInfo = CommandParser(searchWord)

        self._re = commandInfo.getRe()
        self._doc = {}
        self._dir = indexDir
        self._searchWord = commandInfo.getWords()
        self._words = commandInfo.getWords()
        self._resultSentencesList = []
        self._match = []
        self._fields = commandInfo.getFields()

    def search(self):
        indexDir = SimpleFSDirectory(Paths.get(self._dir))
        sear = IndexSearcher(DirectoryReader.open(indexDir))
        query = QueryParser('doc', StandardAnalyzer()).parse(make_parser(self._searchWord))
        hits = sear.search(query, 9999)
        for hit in hits.scoreDocs:
            doc = sear.doc(hit.doc)
            res = doc.get('doc')
            id = doc.get('doc_id')
            self._doc[id] = res
            if doc_hit(res, self._words):
                sentences = re.split('[!?！？。]', res)
                for i in range(sentences.count('')):
                    sentences.remove('')
                for sentence in sentences:
                    f = key_filter(self._words, self._re, sentence)
                    if f:
                        self._match.append(f)
                        self._resultSentencesList.append((id, sentence))
        return self

    def searchAncient(self, field):
        indexDir = SimpleFSDirectory(Paths.get(self._dir))
        sear = IndexSearcher(DirectoryReader.open(indexDir))
        bq = BooleanQuery.Builder()
        q = QueryParser(field, StandardAnalyzer()).parse(make_parser(self._searchWord))
        bc = BooleanClause(q, BooleanClause.Occur.MUST)
        bq.add(bc)
        search_fields = self._fields
        for i in search_fields:
            if i == 'section' or i == 'document':
                continue
            queryx = QueryParser(i, KeywordAnalyzer()).parse(make_ancient_parser(search_fields[i]))
            bc = BooleanClause(queryx, BooleanClause.Occur.MUST)
            bq.add(bc)
        query = bq.build()
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
            self._doc[id] = res
            if doc_hit(res, self._words):
                f = key_filter(self._words, self._re, res)
                if f:
                    if 'section' in search_fields.keys():
                        if not search_upper_title_filter(id, sear, search_fields['section'], 0):
                            continue
                    if 'document' in search_fields.keys():
                        if not search_upper_title_filter(id, sear, search_fields['document'], 1):
                            continue
                    self._match.append(f)
                    self._resultSentencesList.append((id, res, detail, zhujie))
                    print(res)
                    print(self._match)
        return self

    def getResult(self, left: int, right: int):
        result_list = []
        i = 0
        for r in self._resultSentencesList:
            doc = self._doc[r[0]]
            s_position = doc.find(r[1])
            imp_word = self._match[i]
            i += 1
            mid_beg = s_position + r[1].find(imp_word)
            mid_end = mid_beg + len(imp_word) + 1
            s_m = doc[mid_beg:mid_end - 1]
            if mid_beg - left >= 0:
                s_l = doc[mid_beg - left:mid_beg]
            else:
                s_l = doc[0:mid_beg]
            if mid_beg + right <= len(doc):
                s_r = doc[mid_end - 1:mid_end + right]
            else:
                s_r = doc[mid_end-1:len(doc)]
            s_beg = s_position
            s_end = s_beg + len(r[1]) + 1
            result_list.append({'left': s_l, 'right': s_r, 'mid': s_m, 'id': r[0], 'beg': s_beg, 'end': s_end, 'detail': r[2], 'zhujie': r[3]})
        return result_list


def make_parser(words: list):
    res = ''
    for w in words:
        res += w + ' AND '
    res = res[0:-5]
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


def doc_hit(doc: str, words: list):
    for w in words:
        p = doc.find(w)
        if p < 0:
            return False
    return True


def key_filter(words: list, r:str, sentence: str):
    for word in words:
        p = sentence.find(word)
        if p < 0:
            return False
    s = re.search(r, sentence)
    if not s:
        return False
    return s.group(0)


if __name__ == '__main__':
    lucene.initVM()
    # print(make_parser(PatternSearcher('是(v,<5)沒(t)', './index_ancient/')._searchWord))
    print(PatternSearcher('是(v,<5)沒(t) author:皇侃', '../index_ancient/').searchAncient('text').getResult(30,30))