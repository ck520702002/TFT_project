from django.conf.urls import patterns, url
from posts.views import PostView,DiscussPost,PostDetail
from posts import views

urlpatterns = patterns('',
<<<<<<< HEAD
	url(r'^$', PostView.as_view(success_url= "/posts" ), name="create" ),
	#url(r'^list/$', ShowPost.as_view()),
=======
	url(r'^$', PostView.as_view(success_url= "list" ), name="create" ),
	url(r'^list/$', ShowPost.as_view()),
>>>>>>> parent of e98f81f... 結合po文與文章列表
	url(r'^list/(?P<pk>\d+)/detail/$', PostDetail.as_view())
 )
