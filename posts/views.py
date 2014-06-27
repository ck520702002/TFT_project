from django.template import RequestContext, loader
from django.http import HttpResponse
from posts.models import Post
from django.views import generic
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

class PostView(CreateView,ListView):
	model = Post
	template_name = 'post_create.html'

class DiscussPost(ListView):
	model = Post
	template_name = 'discuss.html'

class PostDetail(DetailView):
	model = Post
	template_name = 'post_detail.html'



