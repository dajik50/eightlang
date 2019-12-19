from django.conf.urls import url
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/car/
    url(r'^$',views.car_index),
    url(r'^liuyan',views.liuyan)
]