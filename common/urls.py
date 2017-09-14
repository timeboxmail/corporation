#coding:utf-8

from django.conf.urls import url
from common.views import *

urlpatterns=[
    url(r'^$',index,name='index')
]
