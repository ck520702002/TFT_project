from django.conf.urls import patterns, include, url
from django.contrib import admin
from posts.views import PostView,ShowPost
from userena import views as userena_views
admin.autodiscover()

from views import IndexView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', IndexView.as_view(), name='main_base.html'),
    # url(r'^blog/', include('blog.urls')), 
    url(r'^accounts/signup', userena_views.signup,{'success_url':'/'}),
	url(r'^accounts/', include('userena.urls')),
	url(r'^admin/', include(admin.site.urls)),
	
	#url(r'^posts/', PostView.as_view(success_url = "results")),
	url(r'^posts/', include('posts.urls',namespace = "post"))
	url(r'^discuss/', ShowPost.as_view())
)
