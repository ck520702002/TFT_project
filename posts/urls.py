from django.conf.urls import patterns, url
from posts.views import PostView,DiscussPost,PostDetail,ShowPost
from posts import views

urlpatterns = patterns('',

	url(r'^$', PostView.as_view(success_url= "list" ), name="create" ),
	url(r'^list/$', ShowPost.as_view()),

	url(r'^list/(?P<pk>\d+)/detail/$', PostDetail.as_view())
 )
