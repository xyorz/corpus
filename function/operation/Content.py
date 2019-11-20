import sys, os, lucene, json
from java.nio.file import Paths
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.index import \
    FieldInfo, IndexWriter, IndexWriterConfig, IndexOptions, DirectoryReader, IndexReader
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.search import IndexSearcher, WildcardQuery
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.analysis.core import KeywordAnalyzer
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'\\..\\')


def get_content(id, beg, end, dir):
    index_dir = SimpleFSDirectory(Paths.get(dir))
    searcher = IndexSearcher(DirectoryReader.open(index_dir))
    query = QueryParser('doc_id', KeywordAnalyzer()).parse(id)
    hits = searcher.search(query, 9999)
    last_ind = 0
    next_ind = 0
    res = ''
    for hit in hits.scoreDocs:
        doc = searcher.doc(hit.doc)
        res = doc.get('doc')
        last_ind = max(res.rfind('。', 0, beg-1), res.rfind('!', 0, beg-1), res.rfind('?', 0, beg-1),
                       res.rfind('！', 0, beg-1), res.rfind('？', 0, beg-1))
        t = []
        for i in [res.find('。', end), res.find('!', end), res.find('?', end),
                       res.find('！', end), res.find('？', end)]:
            if i > 0:
                t.append(i)
        if len(t) == 0:
            next_ind = -1
        else:
            next_ind = min(t)
    if last_ind == -1:
        if beg > 0:
            last_s = res[0:beg]
        else:
            last_s = ''
    else:
        last_s = res[last_ind+1: beg]
    if next_ind == -1:
        if end == len(res):
            next_s = ''
        else:
            next_s = res[end:]
    else:
        next_s = res[end: next_ind+1]
    this_s = res[beg: end]
    return {'last': last_s, 'this': this_s, 'next': next_s}


def get_ancient_content(id, dir, show_length=300):
    index_dir = SimpleFSDirectory(Paths.get(dir))
    searcher = IndexSearcher(DirectoryReader.open(index_dir))

    text_section = ''
    text_document = ''
    section_id = id[0: id.find('.')]
    query = QueryParser('id', KeywordAnalyzer()).parse(section_id)
    hits = searcher.search(query, 1)
    for hit in hits.scoreDocs:
        doc = searcher.doc(hit.doc)
        document = doc.get('document')
        section = doc.get('section')
        print(section)
        text_document = document
        text_section = section or ''

    text_current = ''
    current_id = int(id[id.rfind('.')+1:])
    search_id = id[0:id.rfind('.')] + '.' + str(current_id)
    query = QueryParser('id', KeywordAnalyzer()).parse(search_id)
    hits = searcher.search(query, 9999)
    for hit in hits.scoreDocs:
        doc = searcher.doc(hit.doc)
        doc_detail = get_detail(doc)
        if doc_detail['text']:
            text_current = add_tag(doc_detail)

    text_before = ''
    text_before_res = ''
    t_id = id
    t_cid = 0
    current_id = int(id[id.rfind('.') + 1:])
    if current_id > 1:
        should_break = False
        while t_cid < current_id-1 and not should_break:
            t_cid += 1
            search_id = id[0:id.rfind('.')] + '.' + str(t_cid)
            query = QueryParser('id', KeywordAnalyzer()).parse(search_id)
            hits = searcher.search(query, 9999)
            for hit in hits.scoreDocs:
                doc = searcher.doc(hit.doc)
                doc_detail = get_detail(doc)
                t_bf_len = len(text_before)
                text_before += doc_detail['text']
                t = False
                offset = False
                if len(text_before) > show_length:
                    t = text_before[-(show_length-t_bf_len):]
                    offset = t_bf_len
                    should_break = True
                if doc_detail['text']:
                    text_before_res += add_tag(doc_detail, t, offset)
    while len(text_before) < show_length:
        t_text_res = ''
        text_list = []
        if int(id.split('.')[1]) > 1:
            current_id = 0
            has_res = True
            while has_res:
                current_id += 1
                search_id = id.split('.')[0] + '.' + str(int(id.split('.')[1])-1) + '.' + str(current_id)
                query = QueryParser('id', KeywordAnalyzer()).parse(search_id)
                hits = searcher.search(query, 9999)
                if len(hits.scoreDocs) == 0:
                    has_res = False
                for hit in hits.scoreDocs:
                    doc = searcher.doc(hit.doc)
                    doc_detail = get_detail(doc)
                    # t_text += doc_detail['text']
                    text_list.append(doc_detail)
                    # if len(t_text + text_before) > show_length:
                    #     t = t_text[len(t_text) - (len(t_text + text_before) - show_length):]

                    # if doc_detail['text']:
                    #     t_text_res += add_tag(doc_detail, t)
        else:
            break

        text_list.reverse()
        text_res_list = []
        # print(text_list)
        t_text = text_before
        for t in text_list:
            t_len_text = len(t_text)
            t_text += t['text']
            tt = False
            offset = False
            if len(t_text) > show_length:
                tt = t_text[-(show_length-t_len_text):]
                # print(show_length)
                # print(t_len_text)
                # print(len(t_text))
                offset = (show_length-len(t_text))
                # offset = -174
                # offset=0
            text_res_list.append(add_tag(t, tt, offset))
            if tt != False:
                break
        text_res_list.reverse()
        for t in text_res_list:
            t_text_res = t_text_res + t

        text_before = t_text + text_before
        text_before_res = t_text_res + "<br>" + text_before_res
        spl_res = id.split('.')
        id = spl_res[0] + '.' + str(int(spl_res[1]) - 1) + '.1'
    text_next = ''
    text_next_res = ''
    id = t_id
    current_id = int(id[id.rfind('.')+1:])
    current_id += 1
    search_id = id[0:id.rfind('.')] + '.' + str(current_id)
    query = QueryParser('id', KeywordAnalyzer()).parse(search_id)
    hits = searcher.search(query, 9999)
    for hit in hits.scoreDocs:
        doc = searcher.doc(hit.doc)
        doc_detail = get_detail(doc)
        text_next += doc_detail['text']
        if doc_detail['text']:
            t = False
            if len(text_next) > show_length:
                t = text_next[0: show_length]
            text_next_res += add_tag(doc_detail, t, 0)
    while len(text_next) < show_length:
        has_res = True
        should_break = False
        if not should_break:
            while has_res:
                current_id += 1
                search_id = id.split('.')[0] + '.' + str(int(id.split('.')[1])) + '.' + str(current_id)
                query = QueryParser('id', KeywordAnalyzer()).parse(search_id)
                hits = searcher.search(query, 9999)
                if len(hits.scoreDocs) == 0:
                    has_res = False
                    # x.x.1直接没有结果，break循环
                    if current_id == 1:
                        should_break = True
                for hit in hits.scoreDocs:
                    doc = searcher.doc(hit.doc)
                    doc_detail = get_detail(doc)
                    t_len = len(text_next)
                    in_text = False
                    text_next += doc_detail['text']
                    if len(text_next) > show_length:
                        in_text = text_next[t_len: show_length]
                    if doc_detail['text']:
                        text_next_res += add_tag(doc_detail, in_text, 0)
                    if len(text_next) > show_length:
                        in_text += '...'
                        should_break = True
                        break
        else:
            break
        text_next_res += '<br>'
        spl_res = id.split('.')
        id = spl_res[0] + '.' + str(int(spl_res[1]) + 1) + '.1'
        current_id = 0
        # text_next_res += "</br>"
    return {'document': text_document, 'section': text_section, 'last': text_before_res, 'this': text_current, 'next': text_next_res}


def get_detail(doc):
    text = doc.get('text') or ''
    type = doc.get('type')
    author = doc.get('author')
    area = doc.get('area')
    dynasty = doc.get('dynasty')
    detail = doc.get('detail')
    zhujie = doc.get('zhujie')
    if detail:
        detail = json.loads(detail, encoding='utf-8')
    else:
        detail = {detail: {}}
    if zhujie:
        zhujie = json.loads(zhujie, encoding='utf-8')
    else:
        zhujie = {}
    return {'text': text, 'type': type, 'author': author, 'area': area, 'dynasty': dynasty, 'detail': detail, 'zhujie': zhujie}


def add_tag(doc_detail, t=False, zhujie_offset=False):
    text_color = 'black'
    if doc_detail['type'] == '原文':
        text_color = "black"
    elif doc_detail['type'] == '注解':
        text_color = "green"
    elif doc_detail['type'] == '义疏':
        text_color = "skyblue"
    detail = doc_detail['detail']
    zhujie = doc_detail['zhujie']
    detail['author'] = doc_detail['author']
    detail['area'] = doc_detail['area']
    detail['dynasty'] = doc_detail['dynasty']
    detail = json.dumps(detail)
    zhujie_empty = len(zhujie.keys()) == 0
    if zhujie_empty:
        zhujie_empty = ''
    else:
        zhujie_empty = 'zhujie'
    if t == False:
        text = doc_detail['text']
    else:
        text = t
    if zhujie_offset != False and 'zhujie' in zhujie:
        zhujie_del_list = []
        for z in zhujie['zhujie']:
            z['offset'] = str(int(z['offset']) + zhujie_offset)
            if int(z['offset']) >= len(text) or int(z['offset']) < 0:
                zhujie_del_list.append(z)
        for d in zhujie_del_list:
            zhujie['zhujie'].remove(d)
    zhujie = json.dumps(zhujie)
    text = '<span class="detail ' + zhujie_empty + '" style="color: ' + text_color + '" data-detail=\'' + detail + '\' data-zhujie=\'' + zhujie + '\'>' + text + '</span>'
    return text


if __name__ == '__main__':
    lucene.initVM()
    print(get_ancient_content('1.1.1', './index_ancient/'))