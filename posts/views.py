from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from posts.models import Post
from django.http import Http404
from django.shortcuts import render_to_response
from django.views.generic.edit import CreateView

class PostView(CreateView):
	model = Post
	template_name = 'post_create.html'
