from django.views.generic.base import TemplateView
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