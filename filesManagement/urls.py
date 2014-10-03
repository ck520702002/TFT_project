# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import *

urlpatterns = patterns('filesManagement.views',
    #url(r'^list/$', 'list', name='list'),
    url(r'^accounts/(?P<username>[\.\w-]+)/$',ShowFolders.as_view()),
    url(r'^$', 'list', name='list'),
)
