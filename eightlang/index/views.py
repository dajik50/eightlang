from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page


# @cache_page(3600*5)
def index(request):
    import random
    uid = request.session.get('uid')
    if not uid:
        target_list = ['sport/','movie/','music/','bookstore/','food/','car/']

        target_url = random.sample(target_list,3)

        return render(request,'index/index.html',locals())
    return render(request, 'index/index.html')
