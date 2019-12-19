from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.food),
    url(r'^kind$', views.kind_food),
    url(r'^good$', views.click_good),
    url(r'^good_next$', views.click_good_next),
    url(r'^zym$', views.zym_food),
    url(r'^search$', views.search_food),
    url(r'^liuyan$', views.liuyan),
]
