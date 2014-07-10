from django.template import RequestContext, loader
from django.http import HttpResponse
from posts.models import Post
from accounts.models import MyProfile
from django.views import generic
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from userena.utils import signin_redirect, get_profile_model, get_user_model

class PostView(CreateView,ListView):
	model = Post
	template_name = 'post_create.html'

class ShowPost(ListView):
	model = Post
	template_name = 'discuss.html'

class PostDetail(DetailView):
	model = Post
	template_name = 'post_detail.html'

class ShowFile(ListView):
	model = Post
	template_name = 'files.html'

class PastPost(ListView):
	model = Post
	template_name = 'pastpost.html'


