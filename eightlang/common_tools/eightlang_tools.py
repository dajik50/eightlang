from django.db.models import F
from django.shortcuts import render
from django.views.decorators.cache import cache_page
import base64

from loginAndreg.models import TotalUser


def set_token(data):
    return base64.urlsafe_b64encode((str(data) + 'eightlang').encode()).decode()


def get_token(data):
    return base64.urlsafe_b64decode(str(data).encode()).decode()[-1:-10:-1]


def get_token_id(data):
    return base64.urlsafe_b64decode(str(data).encode()).decode()[-10::-1][::-1]


def check_login(fun):
    """

    :param fun: 试图函数
    :return: 闭包
    """

    # 装饰器(检查用户登录状态用于权限验证)
    def wrapper(request, *args, **kwargs):
        session_e_token = request.session.get('e_token')
        session_sessionid = request.session.get('sessionid')
        if not session_e_token or not session_sessionid:  # 如果session没有uid或者uname检查cookies
            cookie_id = request.COOKIES.get('e_token')
            cookie_se = request.COOKIES.get('sessionid')
            if not cookie_id or not cookie_se:
                err = '您还未登录，请登录'
                return render(request, 'loginAndreg/login.html', locals())
            # 如果cookies里面有uid和uname则回写session
            else:
                target = get_token(cookie_id)
                if target != 'gnalthgie':
                    err = '您还未登录，请登录'
                    return render(request, 'loginAndreg/login.html', locals())
                request.session['e_token'] = cookie_id
                request.session['sessionid'] = cookie_se

                # 回写后执行试图函数
                return fun(request, *args, **kwargs)
        return fun(request, *args, **kwargs)

    return wrapper


def add_hobby(fun):
    """
    用于增加用户的访问次数
    :param fun: 试图函数
    :return:
    """

    def wrapper(request, *args, **kwargs):
        tmp = request.session.get('e_token')
        if not tmp:
            tmp = request.COOKIES.get('e_token')
            if not tmp:
                return fun(request, *args, **kwargs)
        cur = get_token_id(tmp)
        target = TotalUser.objects.filter(id=cur)
        if request.path_info == '/sport/':
            target.update(sport_fangwen=F('sport_fangwen') + 1)
        elif request.path_info == '/music/':
            target.update(music_fangwen=F('music_fangwen') + 1)
        elif request.path_info == '/car/':
            target.update(car_fangwen=F('car_fangwen') + 1)
        elif request.path_info == '/bookstore/':
            target.update(book_fangwen=F('book_fangwen') + 1)
        elif request.path_info == '/movie/':
            target.update(movie_fangwen=F('movie_fangwen') + 1)
        elif request.path_info == '/movie/':
            target.update(food_fangwen=F('food_fangwen') + 1)
        else:
            return fun(request, *args, **kwargs)
        return fun(request, *args, **kwargs)


    return wrapper
