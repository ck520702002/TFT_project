from django.views.generic import TemplateView, CreateView, ListView
from posts.models import Post
from filesManagement.models import Document
import os
from itertools import chain
from django.shortcuts import render, redirect
from posts.models import get_query
from accounts.models import MyProfile
from accounts.models import TFTGroup

class IndexView(TemplateView):
	template_name = "main_base.html"

class LinkView(TemplateView):
    template_name = 'link.html'
    def get_context_data(self, **kwargs):
		context = super(LinkView, self).get_context_data(**kwargs)
		context['bulletins'] = bulletins = Post.objects.filter(tag1='announcement').order_by("-time")
		return context
    	
    
class TeacherInfoOneOnOneView(TemplateView):
    template_name = 'teacher/teacher_info.html'

class TeacherInfoNwMentorView(TemplateView):
    template_name = 'teacher/teacher_info2.html'	

class HomePageView(CreateView, ListView):
	template_name = 'home.html'
	model = Post
	def get_context_data(self, **kwargs):
		context = super(HomePageView, self).get_context_data(**kwargs)
		context['bulletins'] = Post.objects.filter(tag1='announcement').order_by("-time")
		return context	

	def get(self, request, *args, **kwargs):
		if not request.user.has_perm('accounts.view_profile'):
			return render(request, '401.html')
		documents = Document.objects.exclude(doctypeTag="private").order_by("-time")
		posts = Post.objects.all().order_by("-time")
		bulletins = Post.objects.filter(tag1='announcement').order_by("-time")
		datalist = sorted(chain(list(documents), list(posts)),key=lambda instance: instance.time, reverse = True)
		return render(request, self.template_name, {'alldata':datalist, 'bulletins':bulletins})
	
	def post(self, request, *args, **kwargs):
		if not request.user.has_perm('accounts.view_profile'):
			return render(request, '401.html')
		searchText = ''
		found_msg = None
		found_file = None
		# deal with search
		if ('search' in request.POST):
			if request.POST['search'].strip():
				searchText = ''
				found_msg = None
				found_file = None
				found_bulletin = None
				searchText = request.POST['search']
				entry_query = get_query(searchText, ['context', 'title', 'tag1'])
				found_msg = Post.objects.filter(entry_query).order_by('-time')
				entry_query = get_query(searchText, ['docfile', 'doctypeTag'])
				found_file = Document.objects.filter(entry_query).order_by('-time')
				entry_query = get_query(searchText, ['title', 'context'])
				found_bulletin = Bulletin.objects.filter(entry_query).order_by('-time')
				datalist = sorted(chain(list(found_msg), list(found_file), list(found_bulletin)),key=lambda instance: instance.time, reverse = True)
			else:
				datalist = []
			#datalist = found_msg
			return render(request, self.template_name, {'alldata':datalist})
		# deal with create announcement
		elif ( 'announce_title' in request.POST and 'announce_text' in request.POST ):
			newdoc = Post()
			newdoc.title = request.POST['announce_title']
			newdoc.context = request.POST['announce_text']
			newdoc.tag1 = "announcement"
			newdoc.author = MyProfile.objects.get(user=request.user)
			newdoc.save()
			return redirect("/home")


