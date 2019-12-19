"""eightlang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$',include('index.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^logreg/',include('loginAndreg.urls')),
    url(r'^person/',include('person.urls')),
    url(r'^sport/',include('sport.urls')),
    url(r'^movie/',include('movie.urls')),
    url(r'bookstore/',include('bookweb.urls')),
    url(r'^quit',views.quit_),
    url(r'^abus',views.aboutus),
    url(r'^music/',include('music.urls')),
    url(r'^car/',include('car.urls')),
    url(r'^food/',include('food.urls')),
    url(r'^msg/',views.msg)

]
