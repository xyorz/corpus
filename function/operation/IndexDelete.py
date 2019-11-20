import sys, os, lucene
from java.nio.file import Paths
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.document import Document, Field, FieldType, StringField, TextField
from org.apache.lucene.index import \
    FieldInfo, IndexWriter, IndexWriterConfig, IndexOptions, DirectoryReader, IndexReader, Term
from org.apache.lucene.search import RegexpQuery
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.search import IndexSearcher


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
