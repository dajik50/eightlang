from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.music),
    url(r'^mcr$', views.music_mcr),
    url(r'^ninja_turtles$', views.ninja_turtles),
    url(r'^guns_n_roses$',views.guns_n_roses),
    url(r'^arch_enemy$',views.arch_enemy),
    url(r'^liuyan$',views.liuyan)
]
