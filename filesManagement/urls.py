# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('filesManagement.views',
    #url(r'^list/$', 'list', name='list'),
    url(r'^$', 'list', name='list'),
)
