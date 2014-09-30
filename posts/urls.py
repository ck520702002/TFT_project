from django.conf.urls import patterns, url
from posts.views import *
from posts import views

urlpatterns = patterns('',
	
	url(r'^list/$', ShowPost.as_view(success_url= "/posts/list" ), name="create" ),
	url(r'^list/(?P<pk>\d+)/detail/$', PostDetail.as_view()),
	url(r'^list/(?P<pk>\d+)/edit/$', PostEdit.as_view()),
	url(r'^bulletin/list/$', ShowBulletin.as_view()),
	url(r'^bulletin/create/$', PostBulletin.as_view()),
	url(r'^bulletin/(?P<pk>\d+)/detail/$', PostDetail.as_view()),
	url(r'^bulletin/(?P<pk>\d+)/edit/$', EditBulletin.as_view()),
	#url(r'^$', PostView.as_view(success_url= "/posts/list" ), name="create" ),
 )