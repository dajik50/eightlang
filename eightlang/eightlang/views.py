from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from common_tools import eightlang_tools
from loginAndreg.models import TotalUser
def quit_(request):
    response = render(request,'quit_index.html')
    tmp = request.session.get('e_token', 's1')
    if tmp == 's1':
        return response
    del request.session['e_token']
    tmp2 = request.COOKIES.get('e_token', 's1')
    if tmp2 == 's2':
        return response
    response.delete_cookie('e_token')
    return response
@cache_page(3600*24*5)
def aboutus(request):
    return  render(request,'abus.html')
@cache_page(3600*24*5)
def msg(request):
    return render(request,'msg.html')
