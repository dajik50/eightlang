from django.conf.urls import url,include

from loginAndreg import views

urlpatterns = [
    url(r'^log$',views.login),
    url(r'^reg$',views.reg)

]