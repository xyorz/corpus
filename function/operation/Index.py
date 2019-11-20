import sys, os, lucene, re
from java.nio.file import Paths
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.document import Document, Field, FieldType, StringField, TextField
from org.apache.lucene.index import \
    FieldInfo, IndexWriter, IndexWriterConfig, IndexOptions, DirectoryReader, IndexReader
from org.apache.lucene.store import SimpleFSDirectory
import xml.etree.ElementTree as ET
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/../')


class Index(object):
    def __init__(self, indexDir: str, sourceDocDir: str):
        self._indexDir = indexDir
        self._sourceDorDir = sourceDocDir
        # with open(index_writer_dir, 'r', encoding='utf-8') as file:
        #     self._counter = file.read()

    def create(self):
        index_dir = SimpleFSDirectory(Paths.get(self._indexDir))
        config = IndexWriterConfig(StandardAnalyzer())
        index_writer = IndexWriter(index_dir, config)
        index_writer.deleteAll()
        id = 0
        for file_name in os.listdir(self._sourceDorDir):
            with open(self._sourceDorDir + file_name, 'r', encoding='utf-8') as file:
                doc = file.read()
                document = Document()
                document.add(Field("doc_id", str(id), StringField.TYPE_STORED))
                document.add(Field("doc", doc, TextField.TYPE_STORED))
                index_writer.addDocument(document)
            id += 1
        index_writer.commit()
        index_writer.close()
        # with open(index_writer_dir, 'w+', encoding='utf-8') as file:
        #     file.write(str(int(self._counter) + id))

    def createAncient(self):
        index_dir = SimpleFSDirectory(Paths.get(self._indexDir))
        config = IndexWriterConfig(StandardAnalyzer())
        index_writer = IndexWriter(index_dir, config)
        index_writer.deleteAll()
        counter = 0
        for file_name in os.listdir(self._sourceDorDir):
            counter += 1
            with open(self._sourceDorDir + file_name, 'r', encoding='utf-8') as file:
                doc = file.read()
                root = ET.fromstring(doc)
                document = Document()
                for info in root.iter('文档'):
                    document.add(Field("id", info.attrib['id'], StringField.TYPE_STORED))
                    document.add(Field("document", info.attrib['标题'], StringField.TYPE_STORED))
                    if '作者' in info.attrib.keys():
                        document.add(Field("author", info.attrib['作者'], StringField.TYPE_STORED))
                    if '时期' in info.attrib.keys():
                        document.add(Field("dynasty", info.attrib['时期'], StringField.TYPE_STORED))
                    if '类别' in info.attrib.keys():
                        document.add(Field("type", info.attrib['类别'], StringField.TYPE_STORED))
                s = ''
                for info in root.iter('备注'):
                    s += info.text
                document.add(Field("remarks", s, TextField.TYPE_STORED))
                index_writer.addDocument(document)
                for info in root.iter('章节'):
                    document = Document()
                    document.add(Field("id", info.attrib['id'], StringField.TYPE_STORED))
                    document.add(Field("section", info.attrib['标题'], TextField.TYPE_STORED))
                    if '作者' in info.attrib.keys():
                        document.add(Field("author", info.attrib['作者'], StringField.TYPE_STORED))
                    if '时期' in info.attrib.keys():
                        document.add(Field("dynasty", info.attrib['时期'], StringField.TYPE_STORED))
                    if '类别' in info.attrib.keys():
                        document.add(Field("type", info.attrib['类别'], StringField.TYPE_STORED))
                    index_writer.addDocument(document)
                for info in root.iter('段'):
                    document = Document()
                    document.add(Field("id", info.attrib['id'], StringField.TYPE_STORED))
                    document.add(Field("text", info.text, TextField.TYPE_STORED))
                    if '作者' in info.attrib.keys():
                        document.add(Field("author", info.attrib['作者'], StringField.TYPE_STORED))
                    if '时期' in info.attrib.keys():
                        document.add(Field("dynasty", info.attrib['时期'], StringField.TYPE_STORED))
                    if '类别' in info.attrib.keys():
                        document.add(Field("type", info.attrib['类别'], StringField.TYPE_STORED))
                    else:
                        document.add(Field("type", '原文', StringField.TYPE_STORED))
                    if '过滤' in info.attrib.keys():
                        document.add(Field("filter", info.attrib['过滤'], StringField.TYPE_STORED))
                    else:
                        document.add(Field("filter", '否', StringField.TYPE_STORED))
                    index_writer.addDocument(document)
                for info in root.iter('句'):
                    document = Document()
                    document.add(Field("id", info.attrib['id'], StringField.TYPE_STORED))
                    document.add(Field("text", info.text, TextField.TYPE_STORED))
                    if '作者' in info.attrib.keys():
                        document.add(Field("author", info.attrib['作者'], StringField.TYPE_STORED))
                    if '时期' in info.attrib.keys():
                        document.add(Field("dynasty", info.attrib['时期'], StringField.TYPE_STORED))
                    if '类别' in info.attrib.keys():
                        document.add(Field("type", info.attrib['类别'], StringField.TYPE_STORED))
                    else:
                        document.add(Field("type", '原文', StringField.TYPE_STORED))
                    if '过滤' in info.attrib.keys():
                        document.add(Field("filter", info.attrib['过滤'], StringField.TYPE_STORED))
                    else:
                        document.add(Field("filter", '否', StringField.TYPE_STORED))
                    index_writer.addDocument(document)
        with open(index_writer_dir, 'w+', encoding='utf-8') as file:
            file.write(str(counter+1))
        index_writer.commit()
        index_writer.close()


if __name__ == "__main__":
    lucene.initVM()
    # Index('../index/index_ancient/', '../document/doc_ancient/').createAncient()
    # Index('../index/index_modern/', '../document/doc_modern/').create()
    # Index('../index/index_ancient/', 'C:/Users/Administrator/Desktop/corpus/doc/').create_ancient_new()
    # with open('./doc_ancient/论语解集义疏.xml', 'r', encoding='utf-8') as file:
    #     doc = file.read()
    #     root = ET.fromstring(doc)
    #     for info in root.iter('文档'):
    #         print(info.attrib['呵呵'])

    def write(document_dir: str, index_writer):
        l = os.listdir(document_dir)
        for i in l:
            if os.path.isfile(document_dir + i) and i.endswith(".utf8"):
                global counter_document
                counter_document += 1
                counter_section = 0
                counter_para = 0
                with open(document_dir + i, 'r', encoding='utf-8') as file:
                    current_author = ""
                    current_dynasty = re.search("[0-9]{2}(.+?)/", document_dir).group(1)
                    line = file.readline()
                    while line:
                        document = Document()
                        if line.find("--d") == 0:
                            document.add(Field("id", str(counter_document), StringField.TYPE_STORED))
                            document.add(
                                Field("document", line.replace("--d", "").replace("\n", ""), StringField.TYPE_STORED))
                            document.add(Field("author", current_author, StringField.TYPE_STORED))
                            document.add(Field("dynasty", current_dynasty, StringField.TYPE_STORED))
                            document.add(Field("type", "原文", StringField.TYPE_STORED))
                            index_writer.addDocument(document)
                        elif line.find("--a") == 0:
                            current_author = line.replace("--a", "").replace("\n", "")
                        elif line.find("--s") == 0:
                            counter_section += 1
                            counter_para = 0
                            id = str(counter_document) + "." + str(counter_section)
                            document.add(Field("id", id, StringField.TYPE_STORED))
                            document.add(
                                Field("section", line.replace("--s", "").replace("\n", ""), StringField.TYPE_STORED))
                            document.add(Field("author", current_author, StringField.TYPE_STORED))
                            document.add(Field("dynasty", current_dynasty, StringField.TYPE_STORED))
                            document.add(Field("type", "原文", StringField.TYPE_STORED))
                            index_writer.addDocument(document)
                        elif line.find("--p") == 0:
                            counter_para += 1
                            id = str(counter_document) + "." + str(counter_section) + "." + str(counter_para)
                            document.add(Field("id", id, StringField.TYPE_STORED))
                            document.add(
                                Field("text", line.replace("--p", "").replace("\n", ""), TextField.TYPE_STORED))
                            document.add(Field("author", current_author, StringField.TYPE_STORED))
                            document.add(Field("dynasty", current_dynasty, StringField.TYPE_STORED))
                            document.add(Field("type", "原文", StringField.TYPE_STORED))
                            index_writer.addDocument(document)
                        line = file.readline()

            elif os.path.isdir(document_dir + i):
                # Index(index, document_dir + i + '/').create_ancient_new()
                write(document_dir + i + "/", index_writer)

    counter_document = 0

    index_dir = SimpleFSDirectory(Paths.get('../index/index_test/'))
    config = IndexWriterConfig(StandardAnalyzer())
    index_writer = IndexWriter(index_dir, config)
    index_writer.deleteAll()

    write('C:/Users/Administrator/Desktop/corpus/doc/06宋/', index_writer)

    index_writer.commit()
    index_writer.close()

