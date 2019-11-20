import sys, os, lucene, json
from java.nio.file import Paths
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.index import \
    FieldInfo, IndexWriter, IndexWriterConfig, IndexOptions, DirectoryReader, IndexReader, Term
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.search import IndexSearcher, WildcardQuery
from org.apache.lucene.search import RegexpQuery
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.analysis.core import KeywordAnalyzer


class CorpusDocList(object):
    def __init__(self, indexDir: str):
        index_dir = SimpleFSDirectory(Paths.get(indexDir))
        self._searcher = IndexSearcher(DirectoryReader.open(index_dir))
        self._resList = []

    def query(self):
        searcher = self._searcher
        query = RegexpQuery(Term('id', '[0-9]+'))
        hits = searcher.search(query, 99999)
        for hit in hits.scoreDocs:
            doc = searcher.doc(hit.doc)
            id = doc.get('id')
            document = doc.get('document')
            author = doc.get('author')
            dynasty = doc.get('dynasty')
            type = doc.get('type')
            update_user = doc.get('username')
            self._resList.append({'id': id, 'document': document, 'author': author, 'dynasty': dynasty, 'type': type, 'update_user': update_user})
        return self

    def result(self):
        return self._resList


class DocumentData(object):
    def __init__(self, id: str, indexDir: str):
        index_dir = SimpleFSDirectory(Paths.get(indexDir))
        self._searcher = IndexSearcher(DirectoryReader.open(index_dir))
        self._id = id
        self._resDict = {}
        self._strDict = ''

    def queryForData(self):
        searcher = self._searcher
        query_document = RegexpQuery(Term('id', str(self._id)))
        hits = searcher.search(query_document, 1)
        document_id = ''
        for hit in hits.scoreDocs:
            doc = searcher.doc(hit.doc)
            document_id = doc.get('id')
            document = doc.get('document')
            author = doc.get('author')
            dynasty = doc.get('dynasty')
            type = doc.get('type')
            color = doc.get('color')
            area = doc.get('area')
            zhujie = doc.get('zhujie')
            if doc.get('detail'):
                detail = json.dumps(json.loads(doc.get('detail'), encoding='utf-8')['detail'])
            else:
                detail = ''
            if not document:
                document = ''
            if not author:
                author = ''
            if not dynasty:
                dynasty = ''
            if not type:
                type = ''
            self._resDict[document_id] = {'document': document, 'author': author, 'dynasty': dynasty, 'type': type, 'color': color, 'area': area, 'detail': detail, 'zhujie': zhujie}
        query_section = RegexpQuery(Term('id', document_id+'\.[0-9]+'))
        hits = searcher.search(query_section, 99999)
        for hit in hits.scoreDocs:
            doc = searcher.doc(hit.doc)
            section_id = doc.get('id')
            section = doc.get('section')
            author = doc.get('author')
            dynasty = doc.get('dynasty')
            type = doc.get('type')
            color = doc.get('color')
            area = doc.get('area')
            zhujie = doc.get('zhujie')
            if doc.get('detail'):
                detail = json.dumps(json.loads(doc.get('detail'), encoding='utf-8')['detail'])
            else:
                detail = ''
            if not section:
                section = ''
            if not author:
                author = ''
            if not dynasty:
                dynasty = ''
            if not type:
                type = ''
            self._resDict[section_id] = {'section': section, 'author': author, 'dynasty': dynasty, 'type': type, 'color': color, 'area': area, 'detail': detail, 'zhujie': zhujie}
        query_paragraph = RegexpQuery(Term('id', document_id+'\.[0-9]+\.[0-9]+'))
        hs = searcher.search(query_paragraph, 99999)
        for h in hs.scoreDocs:
            doc = searcher.doc(h.doc)
            paragraph_id = doc.get('id')
            author = doc.get('author')
            dynasty = doc.get('dynasty')
            type = doc.get('type')
            text = doc.get('text')
            color = doc.get('color')
            area = doc.get('area')
            zhujie = doc.get('zhujie')
            if doc.get('detail'):
                detail = json.dumps(json.loads(doc.get('detail'), encoding='utf-8')['detail'])
            else:
                detail = ''
            if not author:
                author = ''
            if not dynasty:
                dynasty = ''
            if not type:
                type = ''
            if not text:
                text = ''
            self._resDict[paragraph_id] = {'author': author, 'dynasty': dynasty, 'type': type, 'text': text, 'color': color, 'area': area, 'detail': detail, 'zhujie': zhujie}
        return self

    def result_dict(self):
        return self._resDict

    def result_str_dict(self):
        return sort_dict(self._resDict)


def sort_dict(data: dict):
    key_list = []
    res_list = []
    for key in data.keys():
        if key.count('.') == 0:
            key_list.append(key+'.0.0')
        elif key.count('.') == 1:
            key_list.append(key+'.0')
        else:
            key_list.append(key)
    key_list.sort(key=lambda x: int(x.split('.')[2]))
    key_list.sort(key=lambda x: int(x.split('.')[1]))
    key_list.sort(key=lambda x: int(x.split('.')[0]))
    count = 0
    for v in key_list:
        count += 1
        key = v.replace('.0', '')
        res_list.append({key: data[key]})

    str_list = str(res_list)
    str_list = str_list[1:-1]
    str_list = str_list.replace('}, {', ', ')
    return str_list


if __name__ == '__main__':
    # lucene.initVM()
    # print(CorpusDocList('./index_ancient').query().result())
    # print(str(DocumentData('3', '../index/index_ancient').queryForData().result()))
    # test_list = ['1.1.2', '1.3.1', '1.2.3', '1.1.1', '1.2.2', '1.2.1']
    # test_list.sort(key=lambda x: x.split('.')[2])
    # print(test_list)
    # test_list.sort(key=lambda x: x.split('.')[1])
    # print(test_list)
    # test_list.sort(key=lambda x: x.split('.')[0])
    # print(test_list)
    d = {'4': {'type': '', 'document': 'asdasdasd', 'author': '', 'dynasty': ''}, '4.1.3': {'type': '原文', 'text': '', 'author': '', 'dynasty': ''}, '4.1.2': {'type': 'sdasd', 'text': 'sssss', 'author': 'asdsddd', 'dynasty': 'asdads'}, '4.1.1': {'type': '原文', 'text': 'asdsdaasddsa', 'author': 'dasdad', 'dynasty': ''}, '4.1': {'type': '', 'section': 'asdasd', 'dynasty': '', 'author': ''}}
    # print(sort_dict(d))