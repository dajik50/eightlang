from django.conf.urls import url
from . import views
import person.views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^lists$', views.lists),
    url(r'^liuyan$', views.msg_board),
    url(r'^love$', views.love),
    url(r'^city$', views.city),
    url(r'^elfland$', views.elfland),
    url(r'^scifi$', views.scifi),
    url(r'^book_detail', views.book_detail),
    url(r'^book_detail', views.search_book),
    url(r'^dianzancg$', views.sc_book1),
    url(r'^author_detail',views.author_detail),

]
