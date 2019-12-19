from django.http import HttpResponse, Http404
from django.shortcuts import render


# Create your views here.
from common_tools import eightlang_tools
from loginAndreg.models import TotalUser

@eightlang_tools.add_hobby
def car_index(request):
    e_token = request.session.get('e_token')
    if not e_token:
        e_token = request.COOKIES.get('e_token')
        if not e_token:
            nickname = '游客访问'
            return render(request, 'car/car_index.html', locals())
        else:
            uid = eightlang_tools.get_token_id(e_token)
            nickname = '欢迎回来' + str(TotalUser.objects.get(id=uid).nickname)
            return render(request, 'car/car_index.html', locals())
    else:
        uid = eightlang_tools.get_token_id(e_token)
        nickname = '欢迎回来' + str(TotalUser.objects.get(id=uid).nickname)
        return render(request, 'car/car_index.html', locals())


@eightlang_tools.check_login
def liuyan(request):
    if request.method == 'GET':
        target = TotalUser.objects.all()
        messages = []
        for i in target:
            data_1 = list(i.userliuyan_set.values_list('create_time', 'car_liuyan'))  # [(time,content),(),()]
            data_2 = [list(j) for j in data_1 if j[1] != 'null']  # [[],[]]
            for j in data_2:
                j.insert(0, i.nickname)
                messages.append(j)
        return render(request, 'car/liuyan.html', locals())
    if request.method == 'POST':
        e_token = request.COOKIES.get('e_token')
        uid = eightlang_tools.get_token_id(e_token)
        content = request.POST.get('content')
        target = TotalUser.objects.get(id=uid)
        target.userliuyan_set.create(car_liuyan=content)
        return render(request, 'car/liuyan.html')
    return Http404
