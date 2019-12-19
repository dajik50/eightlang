from django.http import Http404
from django.shortcuts import render

# Create your views here.
from common_tools import eightlang_tools
from loginAndreg.models import TotalUser


@eightlang_tools.add_hobby
def index(request):
    if request.method == 'GET':

        e_token = request.session.get('e_token')
        if not e_token:
            e_token = request.COOKIES.get('e_token')
            if not e_token:
                nickname = '游客访问'
                return render(request, 'movie/index.html', locals())
            else:
                uid = eightlang_tools.get_token_id(e_token)
                nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
                return render(request, 'movie/index.html', locals())
        else:
            uid = eightlang_tools.get_token_id(e_token)
            nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
            return render(request, 'movie/index.html', locals())
    if request.method == 'POST':
        pass


def aiqing(request):
    if request.method == 'GET':

        e_token = request.session.get('e_token')
        if not e_token:
            e_token = request.COOKIES.get('e_token')
            if not e_token:
                nickname = '游客访问'
                return render(request, 'movie/aiqing.html', locals())
            else:
                uid = eightlang_tools.get_token_id(e_token)
                nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
                return render(request, 'movie/aiqing.html', locals())
        else:
            uid = eightlang_tools.get_token_id(e_token)
            nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
            return render(request, 'movie/aiqing.html', locals())
    if request.method == 'POST':
        pass


def dongman(request):
    if request.method == 'GET':

        e_token = request.session.get('e_token')
        if not e_token:
            e_token = request.COOKIES.get('e_token')
            if not e_token:
                nickname = '游客访问'
                return render(request, 'movie/dongman.html', locals())
            else:
                uid = eightlang_tools.get_token_id(e_token)
                nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
                return render(request, 'movie/dongman.html', locals())
        else:
            uid = eightlang_tools.get_token_id(e_token)
            nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
            return render(request, 'movie/dongman.html', locals())
    if request.method == 'POST':
        pass


def science_fiction(request):
    if request.method == 'GET':

        e_token = request.session.get('e_token')
        if not e_token:
            e_token = request.COOKIES.get('e_token')
            if not e_token:
                nickname = '游客访问'
                return render(request, 'movie/science_fiction.html', locals())
            else:
                uid = eightlang_tools.get_token_id(e_token)
                nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
                return render(request, 'movie/science_fiction.html', locals())
        else:
            uid = eightlang_tools.get_token_id(e_token)
            nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
            return render(request, 'movie/science_fiction.html', locals())
    if request.method == 'POST':
        pass


def terror(request):
    if request.method == 'GET':

        e_token = request.session.get('e_token')
        if not e_token:
            e_token = request.COOKIES.get('e_token')
            if not e_token:
                nickname = '游客访问'
                return render(request, 'movie/terror.html', locals())
            else:
                uid = eightlang_tools.get_token_id(e_token)
                nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
                return render(request, 'movie/terror.html', locals())
        else:
            uid = eightlang_tools.get_token_id(e_token)
            nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
            return render(request, 'movie/terror.html', locals())
    if request.method == 'POST':
        pass
    return render(request, 'movie/terror.html')


def warfare(request):
    if request.method == 'GET':

        e_token = request.session.get('e_token')
        if not e_token:
            e_token = request.COOKIES.get('e_token')
            if not e_token:
                nickname = '游客访问'
                return render(request, 'movie/warfare.html', locals())
            else:
                uid = eightlang_tools.get_token_id(e_token)
                nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
                return render(request, 'movie/warfare.html', locals())
        else:
            uid = eightlang_tools.get_token_id(e_token)
            nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
            return render(request, 'movie/warfare.html', locals())
    if request.method == 'POST':
        pass

    return render(request, 'movie/warfare.html')


def youth(request):
    if request.method == 'GET':

        e_token = request.session.get('e_token')
        if not e_token:
            e_token = request.COOKIES.get('e_token')
            if not e_token:
                nickname = '游客访问'
                return render(request, 'movie/youth.html', locals())
            else:
                uid = eightlang_tools.get_token_id(e_token)
                nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
                return render(request, 'movie/youth.html', locals())
        else:
            uid = eightlang_tools.get_token_id(e_token)
            nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
            return render(request, 'movie/youth.html', locals())
    if request.method == 'POST':
        pass
    return render(request, 'movie/youth.html')


@eightlang_tools.check_login
def liuyan(request):
    if request.method == 'GET':
        target = TotalUser.objects.all()
        messages = []
        for i in target:
            data_1 = list(i.userliuyan_set.values_list('create_time', 'movie_liuyan'))  # [(time,content),(),()]
            data_2 = [list(j) for j in data_1 if j[1] != 'null']  # [[],[]]
            for j in data_2:
                j.insert(0, i.nickname)
                messages.append(j)
        return render(request, 'movie/liuyan_txt.html', locals())
    if request.method == 'POST':
        e_token = request.COOKIES.get('e_token')
        uid = eightlang_tools.get_token_id(e_token)
        content = request.POST.get('content')
        target = TotalUser.objects.get(id=uid)
        target.userliuyan_set.create(movie_liuyan=content)
        return render(request, 'movie/liuyan_txt.html')
    return Http404
