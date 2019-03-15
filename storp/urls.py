"""commerce URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'storp'
urlpatterns = [
    url(r'^add/$', views.add, name='add'),
    url(r'^list/$', views.list, name='list'),
    url(r'^(?P<s_id>\d+)/update/$', views.update, name='update'),
    url(r'^(?P<s_id>\d+)/detail/$', views.detail, name='detail'),
    url(r'^(?P<s_id>\d+)/(?P<status>\d+)/change/$', views.change, name='change'),
]
