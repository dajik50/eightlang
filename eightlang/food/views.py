from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.db.models import F

# Create your views here.
from django.views.decorators.cache import cache_page

from common_tools import eightlang_tools
from loginAndreg.models import TotalUser
from .models import Food


def click_good(request):
    food_name = request.GET.get('name')
    Food.objects.filter(name=food_name).update(point=F('point') + 1)
    return HttpResponseRedirect('/food/index')


def click_good_next(request):
    # 获取菜系名
    kind = request.GET.get("kind")
    # 获取菜名
    food_name = request.GET.get('name')
    # 对food_name的点赞数加1
    Food.objects.filter(name=food_name).update(point=F('point') + 1)
    return HttpResponseRedirect('/food/kind?name=%s' % kind)

@eightlang_tools.add_hobby
@cache_page(3600*24*5)
def food(request):
    # 获取点赞数最低的10道菜
    index_new_food = Food.objects.all().order_by('point')[:10]
    # 获取点赞数最高的8道菜
    first_four_food_list = Food.objects.all().order_by('-point')[:4]
    late_four_food_list = Food.objects.all().order_by('-point')[4:8]
    return render(request, 'food/index.html', locals())


def kind_food(request):
    # 获取菜系
    name = request.GET.get("name")
    # 获取最新的name菜谱
    new_food = Food.objects.filter(food_kind=name).order_by('point')[:10]
    # 获取前4名的name菜谱
    first_four_food_list = Food.objects.filter(food_kind=name).order_by('-point')[:4]
    # 获取5-8名的name菜谱
    late_four_food_list = Food.objects.filter(food_kind=name).order_by('-point')[4:8]
    if not first_four_food_list or not late_four_food_list or not new_food:
        return Http404
    else:
        return render(request, 'food/kind_food.html', locals())


def zym_food(request):
    # 获取菜名
    name = request.GET.get('name')
    food = Food.objects.filter(name=name)
    tmp=len(food)
    return render(request, 'food/zym_food.html', locals())


def search_food(request):
    if request.method == 'POST':
        name = request.POST.get('search')
        food = Food.objects.filter(name=name)
        tmp = len(food)


        if not food:
            err = '数据库中没有该菜品'
            return render(request, 'food/zym_food.html', locals())
        else:
            return render(request, 'food/zym_food.html', locals())


@eightlang_tools.check_login
def liuyan(request):
    if request.method == 'GET':
        target = TotalUser.objects.all()
        messages = []
        for i in target:
            data_1 = list(i.userliuyan_set.values_list('create_time', 'food_liuyan'))  # [(time,content),(),()]
            data_2 = [list(j) for j in data_1 if j[1] != 'null']  # [[],[]]
            for j in data_2:
                j.insert(0, i.nickname)
                messages.append(j)
        return render(request, 'food/liuyan_txt.html', locals())
    if request.method == 'POST':
        e_token = request.COOKIES.get('e_token')
        uid = eightlang_tools.get_token_id(e_token)
        content = request.POST.get('content')
        target = TotalUser.objects.get(id=uid)
        target.userliuyan_set.create(food_liuyan=content)
        return render(request, 'food/liuyan_txt.html')
    return Http404
