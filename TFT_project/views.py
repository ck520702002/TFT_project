from django.views.generic.base import TemplateView
from posts.models import Post
from filesManagement.models import Document
import os
from itertools import chain

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
		context['documents'] = Document.objects.all().order_by("-time")
		context['posts'] = Post.objects.all().order_by("-time")
		#for data in context['documents']:
			#data.docfile.name = os.path.basename(data.docfile.name)

		datalist = sorted(chain(list(context['documents']), list(context['posts'])),key=lambda instance: instance.time, reverse = True)
		context['alldata'] = datalist
		#print str(context['documents'].count())
		#print str(context['posts'].count())
		#print str(len(datalist))
		return context	