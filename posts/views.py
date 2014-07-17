from django.template import RequestContext, loader
from django.http import HttpResponse
from posts.models import Post
from accounts.models import MyProfile
from django.views import generic
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from userena.utils import signin_redirect, get_profile_model, get_user_model
from django.shortcuts import redirect
from accounts.models import MyProfile

class PostView(CreateView,ListView):
	model = Post
	template_name = 'post_create.html'

class ShowPost(CreateView,ListView):
	model = Post
	#context_object_name = 'posts'
	queryset = Post.objects.all()
	template_name = 'discuss.html'
	'''def get_queryset(self):
        self.post = get_object_or_404(Post, name=self.args[0])
        return Post.objects.filter(post=self.post)'''
	def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
		context = super(ShowPost, self).get_context_data(**kwargs)
    # Add in the publisher
		documents = []
		for document in self.queryset:
			documents.insert(0, document)
		context['posts'] = documents
		return context
	def post(self, request, *args, **kwargs):
		newdoc = Post()
		newdoc.title = request.POST['title']
		newdoc.context = request.POST['context']
		newdoc.tag1 = request.POST['tag1']
		newdoc.author = MyProfile.objects.get(user=request.user)
		newdoc.save()
		return redirect("/posts/list")

class PostDetail(DetailView):
	model = Post
	template_name = 'post_detail.html'

class ShowFile(ListView):
	model = Post
	template_name = 'files.html'

class PastPostDiscuss(ListView):
	model = Post
	template_name = 'pastpost_discuss.html'

class PastPostFile(ListView):
	model = Post
	template_name = 'pastpost_file.html'

class PostEdit(ListView):
	model = Post
	template_name = 'post_edit.html'
