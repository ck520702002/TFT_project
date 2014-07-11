from django.conf.urls import patterns, url
from posts.views import PostView,ShowPost,PostDetail
from posts import views

urlpatterns = patterns('',
	
	url(r'^list/$', ShowPost.as_view(success_url= "/posts/list" ), name="create" ),
	url(r'^list/(?P<pk>\d+)/detail/$', PostDetail.as_view()),
	#url(r'^$', PostView.as_view(success_url= "/posts/list" ), name="create" ),
 )