from django.shortcuts import render
from user.models import CorpusManager
from dmdb import views


root_user = "root"
root_pwd = "root_pwd"
root_auth = 3


def check(name, password):
    manager = CorpusManager.objects.all().filter(login_name=name, password=password).first()
    if not manager:
        if name == root_user and password == root_pwd:
            return 3
        return 0
    return manager.authority


def logout(request):
    if not request.session.get('login_name') or not request.session['password']:
        return login(request)
    del request.session['login_name']
    del request.session['password']
    return login(request)


def login(request):
    if request.method == 'POST':
        login_name = request.POST.get('login_name')
        password = request.POST.get('password')
        manager = CorpusManager.objects.all().filter(login_name=login_name, password=password).first()
        if not manager:
            if login_name != root_user or password != root_pwd:
                return render(request, 'corpus_admin_login.html', {'msg': '用户名或密码错误'})
        request.session['password'] = password
        request.session['login_name'] = login_name
        if login_name == root_user and password == root_pwd:
            request.session['authority'] = root_auth
        else:
            request.session['authority'] = manager.authority
        return views.corpus_manage(request)
    return render(request, 'corpus_admin_login.html')


def delete(request):
    if request.method == 'POST':
        if check(request.session.get('login_name'), request.session.get('password')) < 2:
            return to_index(request)
        authority = request.session.get('authority')
        login_name = request.POST.get('login_name')
        if not login_name:
            return login(request)

        user = CorpusManager.objects.all().filter(login_name=login_name).first()
        if not user:
            return to_manage_page(request, '用户不存在')
        else:
            del_user = CorpusManager.objects.all().filter(login_name=login_name).first()
            del_authority = del_user.authority
            if authority < 3 and del_authority > 1:
                return to_manage_page(request, '权限不足')
            CorpusManager.objects.all().filter(login_name=login_name).delete()
            return to_manage_page(request, '删除成功')
    return login(request)


def add(request):
    if request.method == 'POST':
        if check(request.session.get('login_name'), request.session.get('password')) < 2:
            return to_index(request)
        login_name = request.POST.get('login_name')
        password = request.POST.get('password')
        authority = request.POST.get('authority')
        if not login_name or not password or not authority:
            return login(request)
        try:
            authority = int(authority)
            if authority > 2:
                authority = 2
            elif authority < 1:
                authority = 1
            if not request.session.get('authority') or request.session.get('authority') < 3:
                authority = 1
        except:
            return to_manage_page(request)

        if CorpusManager.objects.all().filter(login_name=login_name):
            return render(request, 'user_add.html', {'msg': '用户名重复'})
        else:
            CorpusManager(login_name=login_name, password=password, authority=authority).save()
        return to_manage_page(request, '添加成功')
    return login(request)


def update(request):
    if request.method == 'POST':
        if check(request.session.get('login_name'), request.session.get('password')) < 2:
            return to_index(request)
        old_name = request.POST.get('old_name')
        login_name = request.POST.get('login_name')
        password = request.POST.get('password')
        authority = request.POST.get('authority')
        if not login_name or not password or not authority or not old_name:
            return login(request)
        try:
            authority = int(authority)
            if authority > 2:
                authority = 2
            elif authority < 1:
                authority = 1
            if not request.session.get('authority') < 3:
                authority = request.session.get('authority')
        except:
            return to_manage_page(request)

        if old_name == login_name:
            CorpusManager.objects.all().filter(login_name=login_name).update(password=password, authority=authority)
            return to_manage_page(request, '修改成功')
        elif CorpusManager.objects.all().filter(login_name=login_name):
            user = CorpusManager.objects.all().filter(login_name=old_name).first()
            if not user:
                return to_manage_page(request, '用户不存在')
            return render(request, 'user_add.html',
                          {'login_name': old_name, 'password': user.password, 'authority': user.authority,
                           'type': 'update', 'msg': '用户名 \"' + login_name + '\" 已存在'})
        else:
            user = CorpusManager.objects.all().filter(login_name=old_name).first()
            if not user:
                return to_manage_page(request, '用户不存在')
            else:
                CorpusManager.objects.all().filter(login_name=old_name).update(login_name=login_name, password=password, authority=authority)
            return to_manage_page(request, '修改成功')
    return to_manage_page(request)


def to_manage_page(request, msg=''):
    if check(request.session.get('login_name'), request.session.get('password')) < 2:
        return to_index(request)
    authority = request.session.get('authority')
    if authority and int(authority) > 0:
        info = CorpusManager.objects.all()
        return render(request, 'user_manage.html', {'info': info, 'msg': msg})
    else:
        return render(request, 'corpus_admin_login.html', {'msg': '权限不足'})


def to_update_page(request):
    if request.method == 'POST':
        login_name = request.POST.get('login_name')
        user = CorpusManager.objects.all().filter(login_name=login_name).first()
        if not user:
            return to_manage_page(request, '用户不存在')
        else:
            return render(request, 'user_add.html', {'login_name': login_name, 'password': user.password, 'authority': user.authority, 'type': 'update'})
    return login(request)


def to_add_page(request):
    return render(request, 'user_add.html', {'type': 'add'})


def to_index(request):
    return render(request, 'corpus_search.html')


def manage_handler(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        login_name = request.POST.get('login_name')
        auth_login_user = request.session.get('authority')
        authority = 1
        if login_name:
            user = CorpusManager.objects.get(login_name=login_name)
            if user:
                authority = user.authority
        if auth_login_user and auth_login_user <= authority:
            return to_manage_page(request, '权限不足')
        if type == '2':
            return to_add_page(request)
        elif type == '1':
            return delete(request)
        elif type == '0':
            return to_update_page(request)
        return to_manage_page(request)
    return login(request)


def update_handler(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        if type == 'add' or type == '':
            return add(request)
        elif type == 'update':
            return update(request)

