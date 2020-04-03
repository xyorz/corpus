import sys, os
from java.nio.file import Paths
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.search import IndexSearcher, TermQuery, RegexpQuery
from org.apache.lucene.index import DirectoryReader, Term
import json
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'\\..\\')


def new_get_content(dir, id, show_length=300):
    index_dir = SimpleFSDirectory(Paths.get(dir))
    searcher = IndexSearcher(DirectoryReader.open(index_dir))
    cur_id_list = [int(x) for x in id.split(".")]
    query = TermQuery(Term("id", ".".join([str(x) for x in cur_id_list])))
    hit = searcher.search(query, 1)
    doc = searcher.doc(hit.scoreDocs[0].doc)
    info_dict = {}
    for field_info in doc.getFields():
        info_dict[field_info.name()] = field_info.stringValue()
    text_cur = [[info_dict]]
    text_prev = []
    cur_id_list[2] -= 1
    while list_text_len(text_prev) < show_length and cur_id_list[1] >= 1:
        para_info = []
        while cur_id_list[2] >= 1:
            query = TermQuery(Term("id", ".".join([str(x) for x in cur_id_list])))
            hit = searcher.search(query, 1)
            doc = searcher.doc(hit.scoreDocs[0].doc)
            info_dict = {}
            for field_info in doc.getFields():
                info_dict[field_info.name()] = field_info.stringValue()
            para_info.insert(0, info_dict)
            cur_id_list[2] -= 1
        text_prev.insert(0, para_info)
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
        over_count = list_text_len(text_prev) - show_length
        len_count = 0
        para_count = 0
        new_para = []
        while True:
            text = text_prev[0][para_count]["text"]
            prev_len = len_count
            len_count += len(text)
            if len_count > over_count:
                text = text[over_count-prev_len:]
                # 修注解的offset
                if "zhujie" in text_prev[0][para_count].keys():
                    zj = json.loads(text_prev[0][para_count]["zhujie"])
                    new_zj_offset = zj["offset"][:]
                    new_zj_content = zj["content"][:]
                    count = 0
                    for i in range(len(zj["offset"])):
                        new_offset = zj["offset"][i] - (over_count-prev_len)
                        if new_offset < 0:
                            new_zj_offset.pop(count)
                            new_zj_content.pop(count)
                            count -= 1
                        else:
                            new_zj_offset[count] = new_offset
                        count += 1
                    text_prev[0][para_count]["zhujie"] = json.dumps({"offset": new_zj_offset, "content": new_zj_content})
                text_prev[0][para_count]["text"] = text
                break
            para_count += 1
        while para_count < len(text_prev[0]):
            new_para.insert(0, text_prev[0][para_count])
            para_count += 1
        text_prev[0] = new_para
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
        para_info = []
        while cur_id_list[2] <= s_id_max:
            query = TermQuery(Term("id", ".".join([str(x) for x in cur_id_list])))
            hit = searcher.search(query, 1)
            doc = searcher.doc(hit.scoreDocs[0].doc)
            info_dict = {}
            for field_info in doc.getFields():
                info_dict[field_info.name()] = field_info.stringValue()
            para_info.append(info_dict)
            # para_text += doc.get("text")
            cur_id_list[2] += 1
        text_next.append(para_info)
        cur_id_list[2] = 1
        cur_id_list[1] += 1
    if len(text_next) > 0 and list_text_len(text_next) >= show_length:
        over_count = list_text_len(text_next) - show_length
        len_count = 0
        para_count = len(text_next[-1]) - 1
        new_para = []
        while True:
            text = text_next[-1][para_count]["text"]
            len_count += len(text)
            if len_count > over_count:
                text = text[:len_count-over_count]
                # 修注解的offset
                if "zhujie" in text_next[-1][para_count].keys():
                    zj = json.loads(text_next[-1][para_count]["zhujie"])
                    new_zj_offset = zj["offset"][:]
                    new_zj_content = zj["content"][:]
                    count = 0
                    for i in range(len(zj["offset"])):
                        if zj["offset"][i] >= len(text):
                            new_zj_offset.pop(count)
                            new_zj_content.pop(count)
                            count -= 1
                        count += 1
                    text_next[-1][para_count]["zhujie"] = json.dumps({"offset": new_zj_offset, "content": new_zj_content})
                text_next[-1][para_count]["text"] = text
                break
            para_count -= 1
        para_count_new = 0
        while para_count_new <= para_count:
            new_para.append(text_next[-1][para_count_new])
            para_count_new += 1
        text_next[-1] = new_para
    if len(text_prev) == 0:
        text_prev = []
    if len(text_cur) == 0:
        text_cur = []
    if len(text_next) == 0:
        text_next = []
    return {"prev": text_prev, "cur": text_cur, "next": text_next}


def list_text_len(text_list: list):
    text_len = 0
    for item in text_list:
        for info in item:
            text_len += len(info["text"])
    return text_len


def get_text_from_content(content):
    [prev, cur, next] = [[], [], []]
    for para in content["prev"]:
        para_text = ""
        for sentence in para:
            para_text += sentence["text"]
        prev.append(para_text)
    for para in content["cur"]:
        para_text = ""
        for sentence in para:
            para_text += sentence["text"]
        cur.append(para_text)
    for para in content["next"]:
        para_text = ""
        for sentence in para:
            para_text += sentence["text"]
        next.append(para_text)
    return {"prev": prev, "cur": cur, "next": next}


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
