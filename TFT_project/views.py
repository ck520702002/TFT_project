from django.views.generic.base import TemplateView
class IndexView(TemplateView):
	template_name = "main_base.html"

class TeacherInfoOneOnOneView(TemplateView):
    template_name = 'teacher/teacher_info.html'

class TeacherInfoNwMentorView(TemplateView):
    template_name = 'teacher/teacher_info2.html'	