from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from loginAndreg.models import TotalUser
from common_tools import eightlang_tools


@eightlang_tools.check_login
def index(request):
    # 选出每个用户的Id以及各种需要的属性
    tmp = request.COOKIES.get('e_token')
    uid = eightlang_tools.get_token_id(tmp)
    cur = TotalUser.objects.get(id=uid)  # queryset
    nickname = '欢迎回来:' + cur.nickname
    target_fangwen = [cur.music_fangwen, cur.car_fangwen, cur.food_fangwen, cur.movie_fangwen, cur.sport_fangwen,
                      cur.book_fangwen]
    target_shequ = ['/music', '/car', '/food', '/movie', '/sport', '/bookstore']
    target_chinese =['音乐社区','汽车社区','美食社区','影视社区','体育社区','图书社区']
    target = dict(zip(target_shequ, target_fangwen))
    print(target)
    target2 =dict(zip(target_shequ,target_chinese))
    result = sorted(target.items(), key=lambda i: i[1], reverse=True)[0:3]
    print(result)
    title = {}
    title[result[0][0]] = target2[result[0][0]]
    title[result[1][0]] = target2[result[1][0]]
    title[result[2][0]] = target2[result[2][0]]
    total_titme = list(title.items())
    print(total_titme)
    total = {'nickname': nickname, 'hobby1': result[0][0], 'hobby2': result[1][0], 'hobby3': result[2][0], 'title1':total_titme[0][1],
             'title2':total_titme[1][1],'title3':total_titme[2][1]}
    return render(request, 'person/person.html', total)


@eightlang_tools.check_login
@cache_page(3600*24*5)
def setting(request):
    if request.method == 'GET':
        return render(request, 'person/setting.html')
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        passwd1 = request.POST.get('passwd')
        passwd2 = request.POST.get('passwd1')
        e_token = request.session.get('e_token')
        # 判断seesion和cookie是否有uid如果没有说明登录过时返回登录页面
        if not e_token:
            c_token = request.COOKIES.get('e_token')
            if not c_token:
                return render(request, 'loginAndreg/login.html')
            request.session['e_token'] = c_token
        if nickname and not passwd1:
            uid = eightlang_tools.get_token_id(e_token)
            target = TotalUser.objects.filter(id=uid)
            target.update(nickname=nickname)
            return render(request, 'person/person.html', locals())
        if passwd1 and passwd2 and not nickname:
            if passwd1 != passwd2:
                err = '两次密码不一致请重新输入!谢谢'
                return render(request, 'person/setting.html', locals())
            uid = eightlang_tools.get_token_id(e_token)
            target = TotalUser.objects.filter(id=uid)
            import hashlib
            md5 = hashlib.md5()
            md5.update(passwd1.encode())
            target.update(passwd=md5.hexdigest())
            err = '已经修改密码请重新登录'
            return render(request, 'loginAndreg/login.html', locals())
        if passwd1 and passwd2 and nickname:
            import hashlib
            md5 = hashlib.md5()
            md5.update(passwd1.encode())
            uid = eightlang_tools.get_token_id(e_token)
            target = TotalUser.objects.filter(id=uid)
            target.update(passwd=md5.hexdigest())
            target.update(nickname=nickname, passwd=md5.hexdigest())
            err = '已经修改密码请重新登录'
            return render(request, 'loginAndreg/login.html', locals())
    err = '请正确输入'
    return render(request, 'person/setting.html', locals())
