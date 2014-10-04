# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import *

urlpatterns = patterns('',
    #url(r'^list/$', 'list', name='list'),
    url(r'^(?P<username>[\.\w-]+)/$',ShowFolders.as_view()),
    url(r'^$', doc_list,name='list'),
)
