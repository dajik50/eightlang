from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page

from common_tools import eightlang_tools
from loginAndreg.models import TotalUser


@eightlang_tools.add_hobby
@cache_page(3600*24*15)
def music(request):

    return render(request, 'music/music_index.html', locals())


@eightlang_tools.check_login
def liuyan(request):
    if request.method == 'GET':
        target = TotalUser.objects.all()
        messages = []
        for i in target:
            data_1 = list(i.userliuyan_set.values_list('create_time', 'musci_liuyan'))  # [(time,content),(),()]
            data_2 = [list(j) for j in data_1 if j[1] != 'null']  # [[],[]]
            for j in data_2:
                j.insert(0, i.nickname)
                messages.append(j)
        return render(request, 'music/liuyan_music.html', locals())
    if request.method == 'POST':
        e_token = request.COOKIES.get('e_token')
        uid = eightlang_tools.get_token_id(e_token)
        content = request.POST.get('content')
        target = TotalUser.objects.get(id=uid)
        target.userliuyan_set.create(musci_liuyan=content)
        return render(request, 'music/liuyan_music.html')
    return Http404


def music_mcr(request):
    return render(request, 'music/music_mcr.html')


def ninja_turtles(request):
    return render(request, 'music/ninja_turtles.html')


def guns_n_roses(request):
    return render(request, 'music/guns_n_roses.html')


def arch_enemy(request):
    return render(request, 'music/arch_enemy.html')
