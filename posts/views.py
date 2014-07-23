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
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from accounts.models import MyProfile
from Msg.models import Message
from posts.models import Post
from posts.models import Bulletin

class PostView(CreateView,ListView):
	model = Post
	template_name = 'post_create.html'

class ShowPost(CreateView,ListView):
	model = Post
	#context_object_name = 'posts'
	template_name = 'discuss.html'
	'''def get_queryset(self):
        self.post = get_object_or_404(Post, name=self.args[0])
        return Post.objects.filter(post=self.post)'''
	def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
		context = super(ShowPost, self).get_context_data(**kwargs)
    # Add in the publisher
		context['posts'] = Post.objects.all().order_by("-time")
		context['bulletins'] = Bulletin.objects.all().order_by("-time")
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
	def get(self, request, *args, **kwargs):
		newdoc = Post.objects.filter(author = request.user).order_by("-time")
		searchPost = Post.objects.get(pk=kwargs['pk'])
		allmsg = Message.objects.filter(belong_post=searchPost).order_by("-time")
		print allmsg
		return render(request, self.template_name, {'post':searchPost, 'allmsg': allmsg, 'bulletins' : Bulletin.objects.all().order_by("-time")})	

	def post(self, request, *args, **kwargs):
		newmsg = Message()
		newmsg.context = request.POST['context']
		newmsg.author = MyProfile.objects.get(user=request.user)
		newmsg.belong_post = Post.objects.get(pk = request.POST['postid'])
		newmsg.save()
		print "qam debug"
		print "postid"+request.POST['postid']
		return redirect("/posts/list/"+request.POST['postid']+"/detail")

class ShowFile(ListView):
	model = Post
	template_name = 'files.html'

class PastPostDiscuss(ListView):
	model = Post
	template_name = 'pastpost_discuss.html'
	def get(self, request, *args, **kwargs):
		newdoc = Post.objects.filter(author = request.user).order_by("-time")
		return render(request, self.template_name, {'posts': newdoc, 'bulletins' : Bulletin.objects.all().order_by("-time")})		
	def post(self, request, *args, **kwargs):
		msgId = request.POST.get('post', None)
		msgToDel = get_object_or_404(Post, pk = msgId)
		msgToDel.delete()
		return redirect("/pastpost_discuss")

class PostEdit(ListView):
	template_name = 'post_edit.html'
	def get(self, request, *args, **kwargs):
		msg = get_object_or_404(Post, pk = kwargs['pk'])
		return render(request, self.template_name, {'post': msg, 'bulletins' : Bulletin.objects.all().order_by("-time")})		
	def post(self, request, *args, **kwargs):
		msgId = request.POST.get('post', None)
		msgToEdit = get_object_or_404(Post, pk = msgId)
		#msgToEdit.update(title = request.POST['title'], context = request.POST['context'], tag1 = request.POST['tag1'])
		msgToEdit.title = request.POST['title']
		msgToEdit.context = request.POST['context']
		msgToEdit.tag1 = request.POST['tag1']
		msgToEdit.save()
		return redirect("/pastpost_discuss")

class PostBulletin(ListView):
	template_name = 'post_bulletin.html'
	def get(self, request, *args, **kwargs):
		bulletin = Bulletin.objects.filter(author = request.user).order_by("-time")
		return render(request, self.template_name, {'bulletins': bulletin})	
	def post(self, request, *args, **kwargs):
		newBulletin = Bulletin()
		newBulletin.title = request.POST['title']
		newBulletin.context = request.POST['context']
		newBulletin.info_url = request.POST['infourl']
		newBulletin.author = MyProfile.objects.get(user=request.user)
		newBulletin.save()
		return redirect("/posts/bulletin/create/")

class ViewBulletin(ListView):
	template_name = 'view_bulletin.html'
	def get(self, request, *args, **kwargs):
		bulletin = Bulletin.objects.filter(author = request.user).order_by("-time")
		data = get_object_or_404(Bulletin, pk = kwargs['pk'])
		return render(request, self.template_name, {'bulletins': bulletin,'data' : data})

class EditBulletin(ListView):
	template_name = 'edit_bulletin.html'
	def get(self, request, *args, **kwargs):
		bulletin = Bulletin.objects.filter(author = request.user).order_by("-time")
		data = get_object_or_404(Bulletin, pk = kwargs['pk'])
		return render(request, self.template_name, {'bulletins': bulletin,'data' : data})
	def post(self, request, *args, **kwargs):
		newBulletin = get_object_or_404(Bulletin, pk = kwargs['pk'])
		newBulletin.title = request.POST['title']
		newBulletin.context = request.POST['context']
		newBulletin.info_url = request.POST['infourl']
		newBulletin.save()
		return redirect("/posts/bulletin/"+kwargs['pk']+"/detail/")

