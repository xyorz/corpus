import sys, os, lucene, json
from java.nio.file import Paths
from org.apache.lucene.index import \
    FieldInfo, IndexWriter, IndexWriterConfig, IndexOptions, DirectoryReader, IndexReader, Term
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.search import IndexSearcher, WildcardQuery
from org.apache.lucene.search import RegexpQuery, TermQuery, BooleanQuery, BooleanClause


class CorpusDocList(object):
    def __init__(self, indexDir: str):
        index_dir = SimpleFSDirectory(Paths.get(indexDir))
        self._searcher = IndexSearcher(DirectoryReader.open(index_dir))

    def query(self):
        searcher = self._searcher
        res_list = []
        query = RegexpQuery(Term('id', '[0-9]+'))
        hits = searcher.search(query, 99999)
        for hit in hits.scoreDocs:
            doc = searcher.doc(hit.doc)
            id = doc.get('id')
            document = doc.get('document')
            sections = doc.get('sections')
            update_user = doc.get('username')
            res_list.append({'id': id, 'document': document, 'sections': sections, 'update_user': update_user})
        return res_list

    def query_by_doc_id(self, doc_id):
        searcher = self._searcher
        query = TermQuery(Term('id', doc_id))
        hits = searcher.search(query, 1)
        doc = searcher.doc(hits.scoreDocs[0].doc)
        document = doc.get('document')
        sections = json.loads(doc.get('sections'))['list']
        return {'document': document, 'list': sections}


class DocumentData(object):
    def __init__(self, id: str, indexDir: str):
        index_dir = SimpleFSDirectory(Paths.get(indexDir))
        self._searcher = IndexSearcher(DirectoryReader.open(index_dir))
        self._id = id
        self._resDict = {}
        self._strDict = ''

    def query_doc(self):
        searcher = self._searcher
        query_document = RegexpQuery(Term('id', str(self._id)))
        top_docs_doc = searcher.search(query_document, 1)
        document_id = str(self._id)
        res_dict = {}
        query_section = RegexpQuery(Term('id', document_id+'\.[0-9]+'))
        top_docs_section = searcher.search(query_section, 99999)
        query_paragraph = RegexpQuery(Term('id', document_id+'\.[0-9]+\.[0-9]+'))
        top_docs_sentence = searcher.search(query_paragraph, 99999)
        top_docs = top_docs_doc.merge(1000000, [top_docs_section, top_docs_doc, top_docs_sentence])
        for hit in top_docs.scoreDocs:
            doc = searcher.doc(hit.doc)
            id = doc.get('id')
            document = doc.get('document')
            section = doc.get('section')
            author = doc.get('author')
            dynasty = doc.get('dynasty')
            type = doc.get('type')
            text = doc.get('text')
            color = doc.get('color')
            area = doc.get('area')
            zhujie = doc.get('zhujie')
            detail = doc.get('detail')
            res_dict[id] = {}
            if document:
                res_dict[id]['document'] = document
            if section:
                res_dict[id]['section'] = section
            if author:
                res_dict[id]['author'] = author
            if dynasty:
                res_dict[id]['dynasty'] = dynasty
            if type:
                res_dict[id]['type'] = type
            if text:
                res_dict[id]['text'] = text
            if color:
                res_dict[id]['color'] = color
            if area:
                res_dict[id]['area'] = area
            if zhujie:
                res_dict[id]['zhujie'] = zhujie
            if detail:
                res_dict[id]['detail'] = detail
        self._resDict = res_dict
        return self

    def query_section(self, section):
        print(section)
        searcher = self._searcher
        query_doc = RegexpQuery(Term('id', self._id+'\\..+'))
        query_section = TermQuery(Term('section', section))
        query = BooleanQuery.Builder()
        bc1 = BooleanClause(query_doc, BooleanClause.Occur.MUST)
        bc2 = BooleanClause(query_section, BooleanClause.Occur.MUST)
        query = query.add(bc1).add(bc2).build()
        top_docs = searcher.search(query, 1000000)
        hits = top_docs.scoreDocs
        res_dict = {}
        for hit in hits:
            doc = searcher.doc(hit.doc)
            id = doc.get('id')
            document = doc.get('document')
            section = doc.get('section')
            author = doc.get('author')
            dynasty = doc.get('dynasty')
            type = doc.get('type')
            text = doc.get('text')
            color = doc.get('color')
            area = doc.get('area')
            zhujie = doc.get('zhujie')
            detail = doc.get('detail')
            res_dict[id] = {}
            if document:
                res_dict[id]['document'] = document
            if section:
                res_dict[id]['section'] = section
            if author:
                res_dict[id]['author'] = author
            if dynasty:
                res_dict[id]['dynasty'] = dynasty
            if type:
                res_dict[id]['type'] = type
            if text:
                res_dict[id]['text'] = text
            if color:
                res_dict[id]['color'] = color
            if area:
                res_dict[id]['area'] = area
            if zhujie:
                res_dict[id]['zhujie'] = zhujie
            if detail:
                res_dict[id]['detail'] = detail
        res_dict[self._id] = {'document': section}
        self._resDict = res_dict
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