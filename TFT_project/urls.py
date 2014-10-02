from django.conf.urls import patterns, include, url
from django.contrib import admin
from posts.views import PostView,ShowPost,PastPostDiscuss
from filesManagement.views import PastPostFile
from userena import views as userena_views
from django.conf.urls.static import static
from django.conf import settings
from TFT_project.views import TeacherInfoOneOnOneView
from TFT_project.views import TeacherInfoNwMentorView
from TFT_project.views import MyFileView, MyDocsView
from TFT_project.views import HomePageView
from accounts.views import profile_edit
from accounts.views import ProfileView
from django.contrib.auth.decorators import login_required
#from filesManagement.views import ShowFile
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from TFT_project.views import LinkView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^/', HomePageView.as_view()),
    # url(r'^blog/', include('blog.urls')), 
    url(r'^accounts/(?P<username>[\.\w-]+)/edit/$', profile_edit, name='userena_profile_edit'),
    url(r'^accounts/(?P<username>[\.\w-]+)/password/$', userena_views.password_change, {'success_url':'/'}),
    url(r'^accounts/signup', userena_views.signup,{'success_url':'/'}),
    url(r'^accounts/view/(?P<pk>\d+)', ProfileView.as_view()),
	url(r'^accounts/', include('userena.urls')),
    #url(r'^accounts/(?P<username>[\.\w-]+)/$',name.get_name ),
	url(r'^admin/', include(admin.site.urls)),
    #url(r'^teacher_info/',include('userena.contrib.teacher_info.urls')),

	#url(r'^posts/', PostView.as_view(success_url = "results")),
	url(r'^posts/', include('posts.urls',namespace = "post")),
	#url(r'^discuss/', ShowPost.as_view()),
    url(r'^pastpost_discuss/', PastPostDiscuss.as_view()),
    url(r'^pastpost_file/', PastPostFile.as_view()),
    url(r'^link', LinkView.as_view()),
    url(r'^myfiles/mydocs', MyDocsView.as_view()),
    url(r'^myfiles/', MyFileView.as_view()),
    url(r'^teacher/oneonone', TeacherInfoOneOnOneView.as_view()),
    url(r'^teacher/nwmentor', TeacherInfoNwMentorView.as_view()),
	#url(r'^posts/', PostView.as_view(success_url = "results")),
	#url(r'^files/', ShowFile.as_view()),
    url(r'^files/', include('filesManagement.urls')),

    #url(r'^accounts/(?P<username>[\.\w-]+)/edit/$',
    #    'userena.views.profile_edit',
    #    {'edit_profile_form': EditProfileFormExtra},
    #    name='userena_profile_edit'),
    url(r'^$', login_required(HomePageView.as_view()), name='main_base.html'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Add media and static files
urlpatterns += staticfiles_urlpatterns()

