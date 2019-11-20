import sys, os, lucene, json
from java.nio.file import Paths
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.index import \
    FieldInfo, IndexWriter, IndexWriterConfig, IndexOptions, DirectoryReader, IndexReader, Term
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.search import IndexSearcher, WildcardQuery
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.analysis.core import KeywordAnalyzer
from org.apache.lucene.search import RegexpQuery


def get_ancient_content(id, dir):
    index_dir = SimpleFSDirectory(Paths.get(dir))
    searcher = IndexSearcher(DirectoryReader.open(index_dir))
    all_text = ''
    query = RegexpQuery(Term('id', id + '\.[0-9]+\.[0-9]+'))
    hits = searcher.search(query, 9999)
    for hit in hits.scoreDocs:
        doc = searcher.doc(hit.doc)
        text = doc.get('text')

    return doc
