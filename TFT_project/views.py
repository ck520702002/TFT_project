from django.views.generic.base import TemplateView
from posts.models import Post
from filesManagement.models import Document
import os
from itertools import chain
from django.shortcuts import render
from posts.models import get_query
from posts.models import Bulletin

class IndexView(TemplateView):
	template_name = "main_base.html"

#class TeacherInfoOneOnOneView(TemplateView):
#    def get(self, request, page, *args, **kwargs):
#        self.template_name = page
#        response = super(TeacherInfoView, self).get(request, *args, **kwargs)
#        try:
#            return response.render()
#        except TemplateDoesNotExist:
#            raise Http404()

class TeacherInfoOneOnOneView(TemplateView):
    template_name = 'teacher/teacher_info.html'

class TeacherInfoNwMentorView(TemplateView):
    template_name = 'teacher/teacher_info2.html'	

class HomePageView(TemplateView):
	template_name = 'home.html'
	def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
		context = super(HomePageView, self).get_context_data(**kwargs)
    # Add in the publisher
		#context['documents'] = Document.objects.all().order_by("-time")
		#context['posts'] = Post.objects.all().order_by("-time")
		#datalist = sorted(chain(list(context['documents']), list(context['posts'])),key=lambda instance: instance.time, reverse = True)
		#context['alldata'] = datalist
		#print str(context['documents'].count())
		#print str(context['posts'].count())
		#print str(len(datalist))
		return context	
	def get(self, request, *args, **kwargs):
		documents = Document.objects.all().order_by("-time")
		posts = Post.objects.all().order_by("-time")
		datalist = sorted(chain(list(documents), list(posts)),key=lambda instance: instance.time, reverse = True)
		return render(request, self.template_name, {'alldata':datalist, 'bulletins' : Bulletin.objects.all().order_by("-time")})
	def post(self, request, *args, **kwargs):
		searchText = ''
		found_msg = None
		found_file = None
		if ('search' in request.POST) and request.POST['search'].strip():
			searchText = request.POST['search']
			entry_query = get_query(searchText, ['context', 'title'])
			found_msg = Post.objects.filter(entry_query).order_by('-time')
			entry_query = get_query(searchText, ['docfile'])
			found_file = Document.objects.filter(entry_query).order_by('-time')
			datalist = sorted(chain(list(found_msg), list(found_file)),key=lambda instance: instance.time, reverse = True)
		else:
			datalist = []
		#datalist = found_msg
		return render(request, self.template_name, {'alldata':datalist, 'bulletins' : Bulletin.objects.all().order_by("-time")})
