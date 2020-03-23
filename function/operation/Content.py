import sys, os
from java.nio.file import Paths
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.search import IndexSearcher, TermQuery, RegexpQuery
from org.apache.lucene.index import DirectoryReader, Term
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'\\..\\')


def new_get_content(dir, id, show_length=300):
    index_dir = SimpleFSDirectory(Paths.get(dir))
    searcher = IndexSearcher(DirectoryReader.open(index_dir))
    cur_id_list = [int(x) for x in id.split(".")]
    query = TermQuery(Term("id", ".".join([str(x) for x in cur_id_list])))
    hit = searcher.search(query, 1)
    doc = searcher.doc(hit.scoreDocs[0].doc)
    text_cur = [doc.get("text")]
    text_prev = []
    cur_id_list[2] -= 1
    while list_text_len(text_prev) < show_length and cur_id_list[1] >= 1:
        para_text = ""
        while cur_id_list[2] >= 1:
            query = TermQuery(Term("id", ".".join([str(x) for x in cur_id_list])))
            hit = searcher.search(query, 1)
            doc = searcher.doc(hit.scoreDocs[0].doc)
            para_text = doc.get("text") + para_text
            cur_id_list[2] -= 1
        text_prev.insert(0, para_text)
        cur_id_list[1] -= 1
        query = RegexpQuery(Term("id", str(cur_id_list[0]) + "\\." + str(cur_id_list[1]) + "\\..+"))
        hits = searcher.search(query, 99999)
        s_id_max = 1
        for hit in hits.scoreDocs:
            doc = searcher.doc(hit.doc)
            s_id = int(doc.get("id").split(".")[2])
            if s_id > s_id_max:
                s_id_max = s_id
        cur_id_list[2] = s_id_max
    if len(text_prev) > 0 and list_text_len(text_prev) >= show_length:
        text_prev[0] = text_prev[0][list_text_len(text_prev)-show_length:]
    cur_id_list = [int(x) for x in id.split(".")]
    text_next = []
    cur_id_list[2] += 1
    while list_text_len(text_next) < show_length:
        query = RegexpQuery(Term("id", str(cur_id_list[0]) + "\\." + str(cur_id_list[1]) + "\\..+"))
        hits = searcher.search(query, 100)
        s_id_max = 1
        if hits.totalHits < 1:
            break
        for hit in hits.scoreDocs:
            doc = searcher.doc(hit.doc)
            s_id = int(doc.get("id").split(".")[2])
            if s_id > s_id_max:
                s_id_max = s_id
        para_text = ""
        while cur_id_list[2] <= s_id_max:
            query = TermQuery(Term("id", ".".join([str(x) for x in cur_id_list])))
            hit = searcher.search(query, 1)
            doc = searcher.doc(hit.scoreDocs[0].doc)
            para_text += doc.get("text")
            cur_id_list[2] += 1
        text_next.append(para_text)
        cur_id_list[2] = 1
        cur_id_list[1] += 1
    if len(text_next) > 0 and list_text_len(text_next) >= show_length:
        text_next[-1] = text_next[-1][:len(text_next[-1])-(list_text_len(text_next)-show_length)]
    if len(text_prev) == 0:
        text_prev = ['']
    if len(text_cur) == 0:
        text_cur = ['']
    if len(text_next) == 0:
        text_next = ['']
    return {"prev": text_prev, "cur": text_cur, "next": text_next}


def list_text_len(text_list: list):
    text_len = 0
    for text in text_list:
        text_len += len(text)
    return text_len


def sort_keys(keys):
    key_list = []
    res_list = []
    for key in keys:
        if key.count('.') == 0:
            key_list.append(key+'.0.0')
        elif key.count('.') == 1:
            key_list.append(key+'.0')
        else:
            key_list.append(key)
    key_list.sort(key=lambda x: int(x.split('.')[2]))
    key_list.sort(key=lambda x: int(x.split('.')[1]))
    key_list.sort(key=lambda x: int(x.split('.')[0]))
    for v in key_list:
        key = v.replace('.0', '')
        res_list.append(key)
    return res_list
