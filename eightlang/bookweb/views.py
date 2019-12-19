import random
import re
from urllib import parse, request

from django.http import Http404
from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
# from guest_book import models
from django.views.decorators.cache import cache_page

from common_tools import eightlang_tools
from loginAndreg.models import TotalUser
from .forms import GuestForm
import json
from .models import Book, Author
from django.db.models import F

ua_list = [
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E) QQBrowser/6.9.11079.201',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)',
    'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50',
]

# Create your views here.
@eightlang_tools.add_hobby
def index(request):
    sc_rank = Book.objects.all().order_by('-stow_number')[:5]
    read_rank = Book.objects.all().order_by('-read_number')[:5]
    time_rank = Book.objects.all().order_by('-up_time')[:5]
    author1 = Author.objects.filter(id=1)
    if len(author1) != 0:
        author1_name = author1[0].author
        author1_content = author1[0].a_decs
        author1_book = author1[0].book_set.all()[0].name

    author2 = Author.objects.filter(id=2)
    if len(author2) != 0:
        author2_name = author2[0].author
        author2_content = author2[0].a_decs
        author2_book = author2[0].book_set.all()[0].name
    author3 = Author.objects.filter(id=3)
    if len(author3) != 0:
        author3_name = author3[0].author
        author3_content = author3[0].a_decs
        author3_book = author3[0].book_set.all()[0].name
    msj_book = Book.objects.filter(name='牧神记')
    if len(msj_book) != 0:
        msj_book = msj_book[0].stow_number
    dgzz_book = Book.objects.filter(name='大国-智能制造')
    if len(dgzz_book) != 0:
        qqgw_book = dgzz_book[0].stow_number
    qqgw_book = Book.objects.filter(name='全能高武')
    if len(qqgw_book) != 0:
        qqgw_book = qqgw_book[0].stow_number
    e_token = request.session.get('e_token')
    if not e_token:
        e_token = request.COOKIES.get('e_token')
        if not e_token:
            nickname = '游客访问'
            return render(request, 'bookweb/index.html', locals())
        else:
            uid = eightlang_tools.get_token_id(e_token)
            nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
            return render(request, 'bookweb/index.html', locals())
    else:
        uid = eightlang_tools.get_token_id(e_token)
        nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
        return render(request, 'bookweb/index.html', locals())


def lists(request):
    e_token = request.session.get('e_token')
    if not e_token:
        e_token = request.COOKIES.get('e_token')
        if not e_token:
            nickname = '游客访问'
            return render(request, 'bookweb/lists.html', locals())
        else:
            uid = eightlang_tools.get_token_id(e_token)
            nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
            return render(request, 'bookweb/lists.html', locals())
    else:
        uid = eightlang_tools.get_token_id(e_token)
        nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
        return render(request, 'bookweb/lists.html', locals())


@eightlang_tools.check_login
def msg_board(request):
    if request.method == 'GET':
        target = TotalUser.objects.all()
        messages = []
        for i in target:
            data_1 = list(i.userliuyan_set.values_list('create_time', 'book_liuyan'))  # [(time,content),(),()]
            data_2 = [list(j) for j in data_1 if j[1] != 'null' ]  # [[],[]]
            for j in data_2:
                j.insert(0, i.nickname)
                messages.append(j)
        return render(request, 'bookweb/liuyan_txt.html', locals())
    if request.method == 'POST':
        e_token = request.COOKIES.get('e_token')
        uid = eightlang_tools.get_token_id(e_token)
        content = request.POST.get('content')
        target = TotalUser.objects.get(id=uid)
        target.userliuyan_set.create(book_liuyan=content)
        return render(request, 'bookweb/liuyan_txt.html')

    return Http404


def love(request):
    sort = 'love'
    all_book = Book.objects.filter(sort=sort)
    e_token = request.session.get('e_token')
    if not e_token:
        e_token = request.COOKIES.get('e_token')
        if not e_token:
            nickname = '游客访问'
            return render(request, 'bookweb/love.html', locals())
        else:
            uid = eightlang_tools.get_token_id(e_token)
            nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
            return render(request, 'bookweb/love.html', locals())
    else:
        uid = eightlang_tools.get_token_id(e_token)
        nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
        return render(request, 'bookweb/love.html', locals())


def city(request):
    sort = 'city'
    all_book = Book.objects.filter(sort=sort)
    e_token = request.session.get('e_token')
    if not e_token:
        e_token = request.COOKIES.get('e_token')
        if not e_token:
            nickname = '游客访问'
            return render(request, 'bookweb/city.html', locals())
        else:
            uid = eightlang_tools.get_token_id(e_token)
            nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
            return render(request, 'bookweb/city.html', locals())
    else:
        uid = eightlang_tools.get_token_id(e_token)
        nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
        return render(request, 'bookweb/city.html', locals())


def elfland(request):
    sort = 'elfland'
    all_book = Book.objects.filter(sort=sort)
    e_token = request.session.get('e_token')
    if not e_token:
        e_token = request.COOKIES.get('e_token')
        if not e_token:
            nickname = '游客访问'
            return render(request, 'bookweb/elfland.html', locals())
        else:
            uid = eightlang_tools.get_token_id(e_token)
            nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
            return render(request, 'bookweb/elfland.html', locals())
    else:
        uid = eightlang_tools.get_token_id(e_token)
        nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
        return render(request, 'bookweb/elfland.html', locals())


def scifi(request):
    sort = 'scifi'
    all_book = Book.objects.filter(sort=sort)
    e_token = request.session.get('e_token')
    if not e_token:
        e_token = request.COOKIES.get('e_token')
        if not e_token:
            nickname = '游客访问'
            return render(request, 'bookweb/sci-fi.html', locals())
        else:
            uid = eightlang_tools.get_token_id(e_token)
            nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
            return render(request, 'bookweb/sci-fi.html', locals())
    else:
        uid = eightlang_tools.get_token_id(e_token)
        nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
        return render(request, 'bookweb/sci-fi.html', locals())


@eightlang_tools.check_login
def book_detail(request):
    book_name = request.GET.get('name')
    one_book = Book.objects.filter(name=book_name)
    author_name = Book.objects.filter(name=book_name)
    tmp =len(author_name)
    result_url = get_url(book_name)
    Book.objects.filter(name=book_name).update(read_number=F('read_number') + 1)
    if len(author_name) != 0:
        author_name = author_name[0].author.author
    else:
        err = "/bookstore"
    e_token = request.session.get('e_token')
    if not e_token:
        e_token = request.COOKIES.get('e_token')
        if not e_token:
            nickname = '游客访问'
            return render(request, 'bookweb/book_detail.html', locals())
        else:
            uid = eightlang_tools.get_token_id(e_token)
            nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
            return render(request, 'bookweb/book_detail.html', locals())
    else:
        uid = eightlang_tools.get_token_id(e_token)
        nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
        return render(request, 'bookweb/book_detail.html', locals())


def get_url(name):
    target = parse.quote(name.encode('gbk'))
    url = 'https://www.9awx.com/modules/article/search.php?searchkey={0}'.format(target)
    r = request.Request(url=url, headers={'User-Agent': random.choice(ua_list)})
    html = request.urlopen(r).read().decode('gbk')
    rgex = r'<td class="odd"><a href="(.*?)">.*?</a></td>'
    try:
        result = re.findall(rgex, html, re.S | re.M)
        result_url = result[0]
        if result_url:
            return result_url
    except IndexError as e:
        return None

def search_book(request):
    a = request.GET.get('name')
    one_book = Book.objects.filter(name=a)
    author_name = Book.objects.filter(name=a)
    if len(author_name) != 0:
        author_name = author_name[0].author.author
    else:
        one_book = '没有找到这本书'
    e_token = request.session.get('e_token')
    if not e_token:
        e_token = request.COOKIES.get('e_token')
        if not e_token:
            nickname = '游客访问'
            return render(request, 'bookweb/book_detail.html', locals())
        else:
            uid = eightlang_tools.get_token_id(e_token)
            nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
            return render(request, 'bookweb/book_detail.html', locals())
    else:
        uid = eightlang_tools.get_token_id(e_token)
        nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
        return render(request, 'bookweb/book_detail.html', locals())


def sc_book1(request):
    name = request.GET.get('name')
    Book.objects.filter(name=name).update(stow_number=F('stow_number') + 1)
    e_token = request.session.get('e_token')
    if not e_token:
        e_token = request.COOKIES.get('e_token')
        if not e_token:
            nickname = '游客访问'
            return render(request, 'bookweb/sc.html', locals())
        else:
            uid = eightlang_tools.get_token_id(e_token)
            nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
            return render(request, 'bookweb/sc.html', locals())
    else:
        uid = eightlang_tools.get_token_id(e_token)
        nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
        return render(request, 'bookweb/sc.html', locals())


def author_detail(request):
    name = request.GET.get('name')
    author = Author.objects.get(author=name)
    author_name = author.author
    author_content = author.a_decs
    author_book = author.book_set.all()

    e_token = request.session.get('e_token')
    if not e_token:
        e_token = request.COOKIES.get('e_token')
        if not e_token:
            nickname = '游客访问'
            return render(request, 'bookweb/author_detail.html', locals())
        else:
            uid = eightlang_tools.get_token_id(e_token)
            nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
            return render(request, 'bookweb/author_detail.html', locals())
    else:
        uid = eightlang_tools.get_token_id(e_token)
        nickname = '欢迎回来:' + str(TotalUser.objects.get(id=uid).nickname)
        return render(request, 'bookweb/author_detail.html', locals())
