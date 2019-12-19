from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^love$', views.aiqing),
    url(r'^dongman$', views.dongman),
    url(r'^kehuan$', views.science_fiction),
    url(r'^terror$', views.terror),
    url(r'^warfare$', views.warfare),
    url(r'^youth$', views.youth),
    url(r'^liuyan',views.liuyan)

]
