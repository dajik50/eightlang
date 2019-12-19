from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from loginAndreg.models import TotalUser
import random
from common_tools import eightlang_tools

@cache_page(60*60*24*5)
def reg(request):
    # 注册试图函数
    if request.method == 'GET':
        # 发送验证码随机数
        num = random.randint(1, 10)
        num1 = random.randint(1, 10)
        num2 = random.randint(5, 10)

        return render(request, 'loginAndreg/reg.html', locals())
    if request.method == 'POST':
        # 发送验证码随机数
        num = random.randint(1, 10)
        num1 = random.randint(1, 10)
        num2 = random.randint(5, 10)
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')
        passwd2 = request.POST.get('passwd2')
        nickname = request.POST.get('nickname')

        if not uname or not passwd or not nickname:
            err = '数据不完整！请重新输入谢谢'
            return render(request, 'loginAndreg/reg.html', locals())
        cur = TotalUser.objects.filter(uname=uname)  # 生成数据库对象
        if cur:
            err = '用户名已存在'
            return render(request, 'loginAndreg/reg.html', locals())
        if passwd != passwd2:
            err = '两次密码输入不一致请核对后重新输入!谢谢'
            return render(request, 'loginAndreg/reg.html', locals())
        import hashlib
        md5 = hashlib.md5()
        md5.update(passwd.encode())
        try:
            TotalUser.objects.create(uname=uname, passwd=md5.hexdigest(), nickname=nickname)
            # 注册成功写入cookie　session
            print(TotalUser.objects.get(uname=uname).id)
            request.session['e_token'] = eightlang_tools.set_token(TotalUser.objects.get(uname=uname).id)
            resp = HttpResponseRedirect('/person')
            resp.set_cookie('e_token', eightlang_tools.set_token(TotalUser.objects.get(uname=uname).id), 3600 * 24 * 15)
            return resp
        except:
            return Http404



@cache_page(60*60*24*5)
def login(request):
    if request.method == 'GET':
        num = random.randint(1, 10)
        num1 = random.randint(1, 10)
        num2 = random.randint(5, 10)

        return render(request, 'loginAndreg/login.html', locals())
    if request.method == 'POST':
        num = random.randint(1, 10)
        num1 = random.randint(1, 10)
        num2 = random.randint(5, 10)
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')
        if not uname or not passwd:
            err = '请正确输入谢谢!'
            return render(request, 'loginAndreg/login.html', locals())
        try:
            cur = TotalUser.objects.get(uname=uname)
        except:
            err = '帐号或密码输入有误,请重新输入'
            return render(request, 'loginAndreg/login.html', locals())
        import hashlib
        md5 = hashlib.md5()
        md5.update(passwd.encode())

        if md5.hexdigest() != cur.passwd:
            err = '帐号或密码输入有误,请重新输入'
            return render(request, 'loginAndreg/login.html', locals())
        # 登录成功后写session cookies
        nickname = cur.nickname

        request.session['e_token'] = eightlang_tools.set_token(TotalUser.objects.get(uname=uname).id)
        resp = HttpResponseRedirect('/person')
        resp.set_cookie('e_token', eightlang_tools.set_token(TotalUser.objects.get(uname=uname).id), 3600 * 24 * 15)
        return resp

    return Http404
