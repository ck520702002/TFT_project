from django.conf.urls import patterns, include, url
from django.contrib import admin
from posts.views import PostView,ShowPost,PastPost
from userena import views as userena_views
from views import IndexView
from django.conf.urls.static import static
from django.conf import settings
#from TFT_project.views import name
from TFT_project.views import TeacherInfoOneOnOneView
from TFT_project.views import TeacherInfoNwMentorView

from accounts.views import profile_edit

#from filesManagement.views import ShowFile


urlpatterns = patterns('',
    # Examples:
    url(r'^$', IndexView.as_view(), name='main_base.html'),
    # url(r'^blog/', include('blog.urls')), 
    url(r'^accounts/(?P<username>[\.\w-]+)/edit/$',
        profile_edit,
        name='userena_profile_edit'),
    url(r'^accounts/(?P<username>[\.\w-]+)/password/$', userena_views.password_change,
        {'success_url':'/'}),
    url(r'^accounts/signup', userena_views.signup,{'success_url':'/'}),
	url(r'^accounts/', include('userena.urls')),
    #url(r'^accounts/(?P<username>[\.\w-]+)/$',name.get_name ),
	url(r'^admin/', include(admin.site.urls)),
    #url(r'^teacher_info/',include('userena.contrib.teacher_info.urls')),

	#url(r'^posts/', PostView.as_view(success_url = "results")),
	url(r'^posts/', include('posts.urls',namespace = "post")),
	url(r'^discuss/', ShowPost.as_view()),
    
    url(r'^pastpost/', PastPost.as_view()),
    url(r'^teacher/oneonone', TeacherInfoOneOnOneView.as_view()),
    url(r'^teacher/nwmentor', TeacherInfoNwMentorView.as_view()),

    #url(r'^files/', ShowFile.as_view()),
    url(r'^files/', include('filesManagement.urls')),



    #url(r'^accounts/(?P<username>[\.\w-]+)/edit/$',
    #    'userena.views.profile_edit',
    #    {'edit_profile_form': EditProfileFormExtra},
    #    name='userena_profile_edit'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
