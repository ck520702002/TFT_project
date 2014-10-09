# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import *

urlpatterns = patterns('',
    #url(r'^list/$', 'list', name='list'),
    url(r'^myfiles/(?P<pk>\d+)/$',folder_detail.as_view()),
    url(r'^myfiles/$', ShowFolders.as_view()),
    url(r'^(?P<pk>\d+)/$',FileDetail.as_view(),name='list'),
    url(r'^$',doc_list.as_view(),name='list'),

)
