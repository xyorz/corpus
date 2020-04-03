import sys, os
from java.nio.file import Paths
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.document import Document, Field, FieldType, StringField, TextField
from org.apache.lucene.index import \
    FieldInfo, IndexWriter, IndexWriterConfig, IndexOptions, DirectoryReader, IndexReader, Term
from org.apache.lucene.search import RegexpQuery
from org.apache.lucene.store import SimpleFSDirectory
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/../')


class IndexUpdate(object):
    def __init__(self, indexDir: str, data: dict, documentCount: str):
        self._dir = indexDir
        self._data = {}
        self._counter = '0'
        # 新建文本
        if '0' in data.keys():
            self._counter = documentCount
            keys = data.keys()
            for key in list(keys):
                if key.find('.') < 0:
                    id_new = self._counter
                else:
                    id_new = self._counter + '.' + key[key.find('.') + 1:]
                data[id_new] = data[key]
                del data[key]
        # 更新文本
        else:
            for key in data.keys():
                if key.count('.') == 0:
                    self._counter = key
        self._data = data

    def update(self):
        delete(self._dir, self._counter)

        index_dir = SimpleFSDirectory(Paths.get(self._dir))
        config = IndexWriterConfig(StandardAnalyzer())
        index_writer = IndexWriter(index_dir, config)

        for key, val in self._data.items():
            document = Document()
            document.add(Field('id', key, StringField.TYPE_STORED))
            # print(key, val)
            for k, v in val.items():
                if v:
                    if k == 'text':
                        document.add(Field('text', v, TextField.TYPE_STORED))
                    else:
                        document.add(Field(k, v, StringField.TYPE_STORED))
            index_writer.addDocument(document)
        index_writer.commit()
        index_writer.close()


def delete(indexDir: str, id: str):
    index_dir = SimpleFSDirectory(Paths.get(indexDir))
    config = IndexWriterConfig(StandardAnalyzer())

    index_writer = IndexWriter(index_dir, config)

    delete_term_query = RegexpQuery(Term('id', id))
    delete_reg_query = RegexpQuery(Term('id', id + '\..*'))

    index_writer.deleteDocuments(delete_term_query)
    index_writer.deleteDocuments(delete_reg_query)
    index_writer.commit()
    index_writer.close()