# -*- coding: utf-8 -*-
from function.operation import Content
from function.operation.corpus_search.NewCorpusSeacher import Searcher as NSearcher
from function.operation.pattern_search.NewPatternSearcher import Searcher as NPSearcher
from function.operation.corpus_search.CorpusErrorReporter import CorpusErrorReporter
from function.operation.pattern_search.PatternErrorReporter import PatternErrorReporter
from function.operation.IndexUpdate import IndexUpdate
from function.operation import IndexDelete
from function.operation.DocumentsDisplay import CorpusDocList, DocumentData
from django.http import JsonResponse, FileResponse, HttpResponse
from django.utils.encoding import escape_uri_path
import lucene, json, sys, threading, traceback, time, datetime

from dmdb.models import AuthorsInfo
from dmdb.models import Var
from dmdb.models import UserAuthorsInfoPreset
from dmdb.models import User
from dmdb.models import ZhToHant

sys.path.append("../..")
lock = threading.Lock()

# Create your views here.

modern_index_dir = './function/index/index_modern'
ancient_index_dir = './function/index/index_ancient'
zh_to_hant_map = {}
for r in ZhToHant.objects.all():
    if r.zh not in zh_to_hant_map:
        zh_to_hant_map[r.zh] = [r.hant]
    else:
        zh_to_hant_map[r.zh].append(r.hant)

# 测试用
user = 'xyorz'
userId = 1


def get_search(keyword, type='normal'):
    initVM()
    if type == 'normal':
        listener = CorpusErrorReporter(keyword)
        if listener.error():
            return {
                "error": True,
                "message": listener.getMessage()
            }
        results = NSearcher(keyword, ancient_index_dir, zh_to_hant_map) \
            .search("text")
    else:
        listener = PatternErrorReporter(keyword)
        if listener.error():
            return {
                "error": True,
                "message": listener.getMessage()
            }
        results = NPSearcher(keyword, ancient_index_dir, zh_to_hant_map) \
            .search('text')
    return {
        "error": False,
        "result": results
    }


def search(request):
    if request.GET.get('keyword'):
        left_length = int(request.GET.get('leftLength'))
        right_length = int(request.GET.get('rightLength'))
        type = request.GET.get('type')
        keyword = request.GET.get('keyword')
        page = int(request.GET.get('page')) - 1
        page_size = int(request.GET.get('pageSize'))
        result = get_search(keyword, type)
        if not result["error"]:
            results = result["result"].get_by_page(page, page_size, (left_length, right_length))
            return JsonResponse(results)
        else:
            return JsonResponse(result)
    else:
        return JsonResponse({
            "error": True,
            "message": "请求格式错误！"
        })


def download_result(request):
    left_length = int(request.GET.get('leftLength'))
    right_length = int(request.GET.get('rightLength'))
    type = request.GET.get('type')
    keyword = request.GET.get('keyword')
    result = get_search(keyword, type)
    if result["error"]:
        return JsonResponse(result)
    results = result["result"].get_by_page(0, 10000, (left_length, right_length))
    file_name = str(datetime.datetime.now().date()) + '-' + str(hash(time.time())) + '.txt'
    res_str = ""
    for doc in results["doc_list"]:
        res_str += "<B>" + doc["document"] + "</B>"
        res_str += doc["left"]
        res_str += "<U>" + doc["mid"] + "</U>"
        res_str += doc["right"]
    response_file = HttpResponse(res_str)
    response = FileResponse(response_file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename={}'.format(escape_uri_path(file_name))
    return response


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


def get_zh_to_hant_list(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        page = int(body['page'])
        all = ZhToHant.objects.all()
        zh_hants = all[(page-1)*10: page*10]
        total = len(all)
        res_list = []
        for i in zh_hants:
            res_list.append({'id': i.id, 'zh': i.zh, 'hant': i.hant})
        return JsonResponse({
            'list': res_list,
            'total': total
        })
    return JsonResponse({
        'success': False
    })


def update_zh_to_hant_1(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        type = body['type']
        if type == 'insert':
            zh = body['zh']
            hant = body['hant']
            ZhToHant(zh=zh, hant=hant).save()
        elif type == 'update':
            id = body['id']
            hant = body['hant']
            ZhToHant.objects.all().filter(id=id).update(hant=hant)
        elif type == 'delete':
            id = body['id']
            ZhToHant.objects.all().filter(id=id).delete()
        else:
            return JsonResponse({'success': False})
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


def new_get_content(request):
    initVM()
    body = json.loads(request.body.decode('utf-8'))
    id = body["id"]
    content = Content.new_get_content(ancient_index_dir, id)
    return JsonResponse(content)


def get_res_statistics(request):
    initVM()
    body = json.loads(request.body.decode('utf-8'))
    type = body["type"]
    keyword = body["keyword"]
    if "field" in body.keys():
        field = body["field"]
    else:
        field = None
    if type == "normal":
        searcher = NSearcher(keyword, ancient_index_dir, zh_to_hant_map).search("text")
        if field:
            res_dict = searcher.get_result_statistics_by_field(field)
        else:
            res_dict = searcher.get_result_statistics_by_keyword()
    else:
        searcher = NPSearcher(keyword, ancient_index_dir, zh_to_hant_map).search("text")
        if field:
            res_dict = searcher.get_result_statistics_by_field(field)
        else:
            res_dict = searcher.get_result_statistics_by_keyword()
    return JsonResponse({
        "dict": res_dict
    })


# id=0新增，>0修改
def corpus_insert(request):
    if request.method == "POST":
        initVM()
        try:
            data = json.loads(request.body.decode('utf-8'), encoding='utf-8')
            # 线程锁，lucene只能一个进程同时写入
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
            traceback.print_exc()
            return JsonResponse({
                "success": False,
                "message": "json解码错误"
            })

    update_user = request.session.get('login_name')
    return JsonResponse({"success": True})


def corpus_manage(request):
    initVM()
    doc_list = CorpusDocList(ancient_index_dir).query()
    return JsonResponse({
        'list': doc_list
    })


def doc(request):
    initVM()
    if request.method == 'POST':
        id = json.loads(request.body.decode('utf-8'))['id']
        data_str = DocumentData(id, ancient_index_dir).query_doc().result_dict()
        return JsonResponse({
            'doc': data_str
        })


def get_section(request):
    initVM()
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        id = body['id']
        section = body['section']
        data_str = DocumentData(id, ancient_index_dir).query_section(section).result_dict()
        return JsonResponse({
            'doc': data_str
        })


def corpus_delete(request):
    initVM()
    if request.method == 'POST':
        id = json.loads(request.body.decode('utf-8'))['id']
        IndexDelete.delete(ancient_index_dir, id)
        doc_list = CorpusDocList(ancient_index_dir).query()
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
        dict_to_append = {
            'id': item.id,
            'author': item.name,
            'dynasty': item.dynasty,
            'type': item.type,
            'color': item.color,
            'area': item.area,
            'preset': preset
        }
        if item.detail:
            dict_to_append["detail"] = item.detail
        res_list.append(dict_to_append)
    return res_list


def authors_info_insert(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        request_list = body['list']
        user = User.objects.all().filter(id=userId).first()
        insert_ids = []
        for item in request_list:
            id, name, dynasty, type, color, preset, area = item['id'], item['author'], item['dynasty'], item['type'], item['color'], item['preset'],  item['area']
            detail = ''
            if 'detail' in item.keys():
                detail = item['detail']

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
        request_list = list(filter(lambda x: True if int(x['id']) > 0 else False, request_list))
        uploaded_list_id = [int(item['id']) for item in request_list]
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
                'info': {
                    'username': request.session.get('username'),
                },
                'success': True
            })
        try:
            body = json.loads(request.body.decode('utf-8'))
            username = body['username']
            password = body['password']
            user = User.objects.all().filter(name=username, pwd=password).first()

            if user:
                request.session['username'] = username
                request.session['password'] = password

                request.session['level'] = user.level
                return JsonResponse({
                    'info': {
                        'username': user.name
                    },
                    'success': True
                })
        except Exception as e:
            traceback.print_exc()
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


def initVM():
    vm_env = lucene.getVMEnv()
    if vm_env:
        vm_env.attachCurrentThread()
    else:
        lucene.initVM(vmargs=['-Djava.awt.headless=true'])

