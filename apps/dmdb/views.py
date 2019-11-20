# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from function.operation import Content
from function.operation.corpus_search.CorpusSearcher import Searcher
from function.operation.pattern_search.PatternSearcher import PatternSearcher
from function.Highlighter import HighLighter
from function.operation.corpus_search.CorpusCommandParser import CommandParser as CorpusCommandParser
from function.operation.corpus_search.CorpusErrorReporter import CorpusErrorReporter
from function.operation.pattern_search.PatternErrorReporter import PatternErrorReporter
from function.operation.IndexUpdate import IndexUpdate
from function.operation import IndexDelete
from function.operation.DocumentsDisplay import CorpusDocList, DocumentData
from function.read_file.Reader import Reader as FileReader
import lucene, time, re
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import FileResponse
from django.utils.encoding import escape_uri_path
import json, sys, os, zipfile, re, threading
from function.encrypt.encrypt import encrypt, decrypt
from dmdb.models import AuthorsInfo
from dmdb.models import Var
from dmdb.models import UserAuthorsInfoPreset
from dmdb.models import User
from dmdb.models import ZhToHant

import xml.etree.ElementTree as ET

from function.zh2Hant import zh2Hant
import function.operation.hant_search as hant_search

import random, string
sys.path.append("../..")
from user import views as user_views
lock = threading.Lock()

# Create your views here.

modern_index_dir = './function/index/index_modern'
ancient_index_dir = './function/index/index_ancient'
index_counter_dir = './function/index/IDCounter.txt'

# 测试用
user = 'xyorz'
userId = 1


# 语料库搜索主功能
def corpus_search(request):

    if request.GET.get('search'):
        initVM()
        t = time.time()
        left_length = request.GET.get('left-length')
        right_length = request.GET.get('right-length')
        type = request.GET.get('search-type')
        search_field = request.GET.get('search-field')
        search_word = request.GET.get('search')
        filter_author = request.GET.get('filter-author')
        filter_dynasty = request.GET.get('filter-dynasty')
        filter_area = request.GET.get('filter-area')
        filter_type = request.GET.get('filter-type')
        filter = {
            'author': filter_author or "",
            'area': filter_area or "",
            'dynasty': filter_dynasty or "",
            'type': filter_type or ""
        }

        search_word_with_filter = search_word

        if filter_author:
            filter_author = filter_author.strip()
            search_word_with_filter += ' author:' + filter_author
        if filter_dynasty and filter_dynasty != "不限":
            filter_dynasty = filter_dynasty.strip()
            search_word_with_filter += ' dynasty:' + filter_dynasty
        if filter_area and filter_area != "不限":
            filter_area = filter_area.strip()
            search_word_with_filter += ' area:' + filter_area
        if filter_type and filter_type != "不限":
            filter_type = filter_type.strip()
            search_word_with_filter += ' type:' + filter_type

        zh_to_hant_words = hant_search.get_res_list(search_word_with_filter, ZhToHant.objects.all())

        # 数值验证
        message = ''
        if not left_length:
            left_length = 30
        if not right_length:
            right_length = 30
        try:
            left_length = int(left_length)
            right_length = int(right_length)
        except ValueError:
            message = "数值错误"
        if type not in ['0', '1']:
            message = "数值错误"
        if search_field not in ['0', '1']:
            message = "数值错误"

        request.session['search_type'] = type
        request.session['search_word'] = search_word
        request.session['search_word_with_filter'] = search_word_with_filter

        if type == '0':
        # 普通查询
            listener = CorpusErrorReporter(search_word_with_filter)
            if listener.error():
                return render(request, 'corpus_search.html',
                              {'keyword': search_word, 'left_length': left_length, 'right_length': right_length,
                               'type': type, 'error_message': listener.getMessage(),
                               'filter': filter})
            hit = []
            # if search_field == '0':
            # for w in zh_to_hant_words:
            #     commandInfo = CorpusCommandParser(w)
            #     hit += Searcher(commandInfo, modern_index_dir).search('doc').getResult(left_length, right_length)
            #     for i in hit:
            #         i['left'] = HighLighter(commandInfo, i['left']).get()
            #         i['right'] = HighLighter(commandInfo, i['right']).get()
            # else:
            commandParserList = []
            for w in zh_to_hant_words:
                commandParserList.append(CorpusCommandParser(w))
                commandInfo = CorpusCommandParser(w)
                hit += Searcher(commandInfo, ancient_index_dir).ancientSearch('text').getResult(left_length, right_length)
            for i in hit:
                left_high_lighter = HighLighter(i['left'])
                right_high_lighter = HighLighter(i['right'])
                for commandInfo in commandParserList:
                    left_high_lighter.add(commandInfo)
                    right_high_lighter.add(commandInfo)
                i['left'] = left_high_lighter.get()
                i['right'] = right_high_lighter.get()

        else:
        # 模式查询
            listener = PatternErrorReporter(search_word_with_filter)
            if listener.error():
                return render(request, 'corpus_search.html', {'keyword': search_word, 'left_length': left_length,
                                                              'right_length': right_length, 'type': type,
                                                              'error_message': listener.getMessage(),
                                                              'filter': filter})
            hit = []
            # if search_field == '0':
            # for w in zh_to_hant_words:
            #     hit += PatternSearcher(w, modern_index_dir).search().getResult(left_length,right_length)
            # else:
            for w in zh_to_hant_words:
                hit += PatternSearcher(w, ancient_index_dir).searchAncient('text').getResult(left_length, right_length)

        if len(hit) == 0:
            return render(request, 'corpus_search.html', {'keyword': search_word, 'no_match': 1,
                                                          'left_length': left_length, 'right_length': right_length,
                                                          'type': type,
                                                          'filter': filter})
        res_list = hit
        pgnt = Paginator(hit, 30)
        page = request.GET.get('page')
        try:
            contacts = pgnt.page(page)
        except PageNotAnInteger:
            contacts = pgnt.page(1)
        except EmptyPage:
            contacts = pgnt.page(pgnt.num_pages)
        return render(request, 'corpus_search.html', {'list': contacts, 'keyword': search_word, 'data': len(res_list),
                                                      'page_list': range(pgnt.num_pages), 'left_length': left_length,
                                                      'right_length': right_length, 'type': type,
                                                      'search_field': search_field, 'cost_time': str(time.time()-t)[0:4],
                                                      'filter': filter
                                                      })
    left_length = 30
    right_length = 30
    return render(request, 'corpus_search.html', {'left_length': left_length, 'right_length': right_length,
                                                  'keyword': '', 'type': '0', 'filter': {}})


# 使用说明页面
def readme(request):
    return render(request, 'readme.html')


def download_readme(request):
    file = open('function/index/使用说明文档.docx', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename={}'.format(escape_uri_path('古汉语语料库检索使用说明文档.docx'))
    return response


def download_backend_readme(request):
    file = open('function/index/古汉语语料库后台管理操作文档.docx', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename={}'.format(escape_uri_path('古汉语语料库后台管理使用说明文档.docx'))
    return response


def all_text(request):
    return render(request, 'all_text.html')


def update_zh_to_hant(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        zh = body['zh']
        update_list = body['list']
        ZhToHant.objects.all().filter(zh=zh).delete()
        querysetlist = []
        for i in update_list:
            querysetlist.append(ZhToHant(zh=zh.encode().decode('utf-8'), hant=i['hant'].encode().decode('utf-8')))
        ZhToHant.objects.bulk_create(querysetlist)
        res_list = []
        for i in ZhToHant.objects.all().filter(zh=zh):
            res_list.append({'id': i.id, 'zh': zh, 'hant': i.hant})
        return JsonResponse({
            'success': True,
            'list': res_list
        })
    return JsonResponse({
        'success': False
    })


def get_hant_by_zh(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        zh = body['zh']
        zh_hants = ZhToHant.objects.all().filter(zh=zh)
        res_list = []
        for i in zh_hants:
            res_list.append({'id': i.id, 'zh': zh, 'hant': i.hant})
        return JsonResponse({
            'list': res_list
        })
    return JsonResponse({
        'success': False
    })


# 获取上下文功能
def corpus_content(request):
    id = request.GET.get('id')
    beg = request.GET.get('beg')
    end = request.GET.get('end')
    if id and beg and end:
        initVM()
        search_field = request.GET.get('field')
        try:
            if search_field == '0':
                res = Content.get_content(id, int(beg), int(end), modern_index_dir)
            else:
                res = Content.get_ancient_content(id, ancient_index_dir)
            search_word = request.session.get('search_word', None)
            search_type = request.session.get('search_type', None)
            zh_to_hant_words = hant_search.get_res_list(search_word, ZhToHant.objects.all())
            last_highlighter = HighLighter(res['last'])
            this_highlighter = HighLighter(res['this'])
            next_highlighter = HighLighter(res['next'])
            for word in zh_to_hant_words:
                last_highlighter.add(CorpusCommandParser(word))
                this_highlighter.add(CorpusCommandParser(word))
                next_highlighter.add(CorpusCommandParser(word))
            if search_word and search_type == '0':
                res['last'] = last_highlighter.get()
                res['this'] = this_highlighter.get()
                res['next'] = next_highlighter.get()
            return JsonResponse(res)
        except:
            JsonResponse({})
    return JsonResponse({})


# 包括新增和更新操作，通过传上来的json数据的id来判断。(0是新增，>0是更新)
def corpus_insert(request):
    if request.method == "POST":
        initVM()
        try:
            data = json.loads(request.body.decode('utf-8'), encoding='utf-8')
            # 线程锁，lucene只能一个进程同时写入
            for key in data.keys():
                if 'detail' in data[key].keys():
                    data[key]['detail'] = json.dumps({'detail': data[key]['detail']})
            lock.acquire()
            count_key = Var.objects.all().filter(key='document_count').first()
            if not count_key:
                Var(key='document_count', value=1).save()
                count = '1'
            else:
                count = count_key.value
            IndexUpdate(ancient_index_dir, data, count).update()
            lock.release()
            Var.objects.all().filter(key='document_count').update(value=int(count)+1)
        except json.decoder.JSONDecodeError:
            message = "json解码错误"

    update_user = request.session.get('login_name')
    return render(request, 'corpus_insert.html', {'user': update_user})


def corpus_manage(request):
    initVM()
    doc_list = CorpusDocList(ancient_index_dir).query().result()
    return JsonResponse({
        'list': doc_list
    })


def doc(request):
    initVM()
    if request.method == 'POST':
        id = json.loads(request.body.decode('utf-8'))['id']
        try:
            int(id)
        except ValueError:
            message = "id数值错误"
            return

        data_str = DocumentData(id, ancient_index_dir).queryForData().result_dict()
        return JsonResponse({
            'doc': json.dumps(data_str, ensure_ascii=False)
        })


def corpus_delete(request):
    initVM()
    if request.method == 'POST':
        id = json.loads(request.body.decode('utf-8'))['id']
        IndexDelete.delete(ancient_index_dir, id)
        doc_list = CorpusDocList(ancient_index_dir).query().result()
        return JsonResponse({
            'docList': doc_list
        })
    return JsonResponse({
        'res': ''
    })


def get_authors_info():
    res_list = []
    user_preset_ids = []
    user = User.objects.all().filter(id=userId).first()
    for item in UserAuthorsInfoPreset.objects.all().filter(user=user):
        user_preset_ids.append(item.authorInfo.id)
    for item in AuthorsInfo.objects.all():
        preset = True if item.id in user_preset_ids else False
        res_list.append({
            'id': item.id,
            'author': item.name,
            'dynasty': item.dynasty,
            'type': item.type,
            'color': item.color,
            'detail': item.detail,
            'area': item.area,
            'preset': preset
        })
    return res_list


def authors_info_insert(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        authors_list = body['list']
        user = User.objects.all().filter(id=userId).first()
        insert_ids = []
        for item in authors_list:
            id, name, dynasty, type, color, preset, area = item['id'], item['author'], item['dynasty'], item['type'], item['color'], item['preset'],  item['area']
            detail = ''
            if 'detail' in item.keys():
                detail = item['detail']
            if detail:
                if isinstance(detail, str):
                    detail = json.loads(detail)
                else:
                    detail = json.dumps({"detail": detail})

            if int(id) < 0 and not AuthorsInfo.objects.all().filter(name=name, dynasty=dynasty, type=type).first():
                AuthorsInfo(name=name, dynasty=dynasty, type=type, color=color, area=area, detail=detail).save()
                author_info = AuthorsInfo.objects.all().filter(name=name, dynasty=dynasty, type=type, color=color, area=area, detail=detail).first()
                insert_ids.append(int(author_info.id))
            else:
                AuthorsInfo.objects.all().filter(id=id).update(name=name, dynasty=dynasty, type=type, color=color, area=area, detail=detail)
                author_info = AuthorsInfo.objects.all().filter(id=id).first()
            user_author_map = UserAuthorsInfoPreset.objects.all().filter(user=user, authorInfo=author_info).first()
            if preset:
                if not user_author_map:
                    UserAuthorsInfoPreset(user=user, authorInfo=author_info).save()
            else:
                if user_author_map:
                    user_author_map.delete()
        authors_id = [int(item.id) for item in AuthorsInfo.objects.all()]
        authors_list = list(filter(lambda x: True if int(x['id']) > 0 else False, authors_list))
        uploaded_list_id = [int(item['id']) for item in authors_list]
        uploaded_list_id.extend(insert_ids)
        for item in authors_id:
            if item not in uploaded_list_id:
                AuthorsInfo.objects.all().filter(id=item).first().delete()

        return JsonResponse({
            'success': True,
            'list': get_authors_info()
        })
    return JsonResponse({

    })


def authors_info(request):
    if request.method == 'POST':
        return JsonResponse({
            'list': get_authors_info()
        })
    return JsonResponse({})


def set_preset(request):
    body = json.loads(request.body.decode('utf-8'))
    type = body['type']
    value = body['value']
    Var(key=type, value=value).save()
    res_value = Var.objects.all().filter(key=type).first().value
    return JsonResponse({
        'type': type,
        'value': res_value
    })


def get_preset(request):
    var_list = Var.objects.all()
    res_list = []
    for item in var_list:
        res_list.append({
            'type': item.key,
            'value': item.value
        })
    return JsonResponse({
        'list': res_list
    })


def login(request):
    if request.method == 'POST':
        if request.session.get('username'):
            return JsonResponse({
                'success': True
            })

        try:
            body = json.loads(request.body.decode('utf-8'))
            iv = request.session.get('iv')
            del request.session['iv']
            if iv:
                data = json.loads(decrypt(body['data'], 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', iv))
            else:
                return JsonResponse({
                    'success': False
                })
            username = data['username']
            password = data['password']
            user = User.objects.all().filter(name=username, pwd=password).first()

            if user:
                request.session['username'] = username
                request.session['password'] = password
                request.session['level'] = user.level
                return JsonResponse({
                    'info': {
                        'nickName': user.nickName
                    },
                    'success': True
                })
        except Exception as e:
            return JsonResponse({
                'success': False
            })
    return JsonResponse({
        'success': False
    })


def logout(request):
    if request.method == 'POST':
        try:
            if request.session.get('username'):
                del request.session['username']
                del request.session['password']
                return JsonResponse({
                    'success': True
                })
        except:
            return JsonResponse({
                'success': False
            })
    return JsonResponse({
        'success': False
    })


def get_iv(request):
    def gen_random_string(slen=16):
        return ''.join(random.sample(string.ascii_letters + string.digits, slen))
    current_iv = gen_random_string()
    request.session['iv'] = current_iv
    return JsonResponse({
        'iv': current_iv
    })


def get_user_list(request):
    level = request.session.get('level')
    if not level or str(level) != '1':
        return JsonResponse({
            'success': False
        })
    user_list = []
    for item in User.objects.all():
        user_list.append({
            'id': item.id,
            'username': item.name,
            'nickName': item.nickName,
            'level': item.level,
        })
    return JsonResponse({
        'list': user_list
    })


def delete_user(request):
    level = request.session.get('level')
    if not level or str(level) != '1':
        return JsonResponse({
            'success': False
        })
    body = json.loads(request.body.decode('utf-8'))
    userid = int(body['id'])
    user = User.objects.all().filter(id=userid).first()
    user.delete()
    user_list = []
    for item in User.objects.all():
        user_list.append({
            'id': item.id,
            'username': item.name,
            'nickName': item.nickName,
            'level': item.level,
        })
    return JsonResponse({
        'success': True,
        'list': user_list
    })


def add_user(request):
    level = request.session.get('level')
    if not level or str(level) != '1':
        return JsonResponse({
            'success': False
        })
    body = json.loads(request.body.decode('utf-8'))
    username, nick_name, password, level = body['username'], body['nickName'], body['password'], body['level']
    if User.objects.all().filter(name=username).first():
        return JsonResponse({
            'success': False,
            'message': '添加失败：用户名已存在'
        })
    User(name=username, nickName=nick_name, pwd=password, level=level).save()
    user_list = []
    for item in User.objects.all():
        user_list.append({
            'id': item.id,
            'username': item.name,
            'nickName': item.nickName,
            'level': item.level,
        })
    return JsonResponse({
        'success': True,
        'list': user_list
    })


def update_user(request):
    body = json.loads(request.body.decode('utf-8'))
    nick_name, password = body['nickName'], body['password']
    username = request.session.get('username')
    if not username:
        return JsonResponse({
            'success': False
        })
    User.objects.all().filter(name=username).update(nickName=nick_name, pwd=password)
    return JsonResponse({
        'success': True
    })


def deactivate(request):
    username = request.session.get('username')
    if not username:
        return JsonResponse({
            'success': False
        })
    user = User.objects.all().filter(name=username).first()
    if str(user.level) == '1':
        if len(User.objects.all().filter(level=1)) == 1:
            return JsonResponse({
                'success': False,
                'message': '这个用户是最后一个管理员，不能注销！'
            })
    del request.session['username']
    del request.session['password']
    del request.session['level']
    return JsonResponse({
        'success': True
    })


def authors_change_preset(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        presetIds = body['list']
        user = User.objects.all().filter(id=userId).first()
        user_presets = UserAuthorsInfoPreset.objects.all().filter(user=user)
        for item in user_presets:
            author_info = AuthorsInfo.objects.all().filter(id=item.authorInfo.id).first()
            user_preset = UserAuthorsInfoPreset.objects.all().filter(user=user, authorInfo=author_info).first()
            if str(user_preset.authorInfo.id) not in presetIds:
                user_preset.delete()
        for item in presetIds:
            author_info = AuthorsInfo.objects.all().filter(id=item).first()
            UserAuthorsInfoPreset(user=user, authorInfo=author_info).save()
        return JsonResponse({
            'success': True,
            'list': get_authors_info()
        })
    return JsonResponse({'success': False})


def files_upload(request):
    def get_namespace(element):
        m = re.match('\{.*\}', element.tag)
        return m.group(0) if m else ''

    if request.method == 'POST':
        files = request.FILES.getlist('files[]')
        for file in files:
            zip = zipfile.ZipFile(file)
            doc = zip.read('word/document.xml').decode('utf-8')
            root = ET.fromstring(doc)

            namespace = get_namespace(root)

            # print(doc.find('//{0}groupId'.format(namespace)).text)

            # for neighbor in root.iter(namespace + 'p'):
            #     print(neighbor.tag)

        return JsonResponse({
            'success': True
        })


def file_analyze(request):

    if request.method == 'POST':
        text = request.body.decode('utf-8')
        text = text.replace('\r', '')
        res = FileReader(text).getInfoDict()
        res['0'] = {'document': '文档标题', 'author': '', 'dynasty': '', 'type': ''}
        res_str = sort_dict(res)
        return HttpResponse(res_str.replace('\'', '\"'))
    return render(request, 'corpus_insert.html')


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
    key_list.sort(key=lambda x: x.split('.')[2])
    key_list.sort(key=lambda x: x.split('.')[1])
    key_list.sort(key=lambda x: x.split('.')[0])
    count = 0
    for v in key_list:
        count += 1
        key = v.replace('.0', '')
        res_list.append({key: data[key]})

    str_list = str(res_list)
    str_list = str_list[1:-1]
    str_list = str_list.replace('}, {', ', ')
    return str_list


def initVM():
    vm_env = lucene.getVMEnv()
    if vm_env:
        vm_env.attachCurrentThread()
    else:
        lucene.initVM(vmargs=['-Djava.awt.headless=true'])

