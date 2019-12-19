from django.db.models import F
from django.http import Http404
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from loginAndreg.models import TotalUser
from common_tools import eightlang_tools
# Create your views here.
# @cache_page(60*15)
@eightlang_tools.add_hobby
def index(request):
    if request.method == 'GET':

        e_token = request.session.get('e_token')
        if not e_token:
            e_token = request.COOKIES.get('e_token')
            if not e_token:
                nickname = '游客访问'
                return render(request,'sport/xly.html',locals())
            else:
                uid = eightlang_tools.get_token_id(e_token)
                nickname = '欢迎回来'+str(TotalUser.objects.get(id=uid).nickname)
                return render(request,'sport/xly.html',locals())
        else:
            uid = eightlang_tools.get_token_id(e_token)
            nickname = '欢迎回来'+str(TotalUser.objects.get(id=uid).nickname)
            return render(request,'sport/xly.html',locals())
    if request.method == 'POST':
        pass

@eightlang_tools.check_login
def liuyan(request):
    if request.method == 'GET':
        target = TotalUser.objects.all()
        messages = []
        for i in target:
            data_1 = list(i.userliuyan_set.values_list('create_time', 'sport_liuyan'))  # [(time,content),(),()]
            data_2 = [list(j) for j in data_1 if j[1] != 'null']  # [[],[]]
            for j in data_2:
                j.insert(0, i.nickname)
                messages.append(j)
        return render(request, 'sport/liuyan_txt.html', locals())
    if request.method == 'POST':
        e_token = request.COOKIES.get('e_token')
        uid = eightlang_tools.get_token_id(e_token)
        content = request.POST.get('content')
        target = TotalUser.objects.get(id=uid)
        target.userliuyan_set.create(sport_liuyan=content)
        return render(request, 'sport/liuyan_txt.html')
    return Http404