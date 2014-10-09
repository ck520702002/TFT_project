# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from filesManagement.models import Document, Folder
from filesManagement.forms import DocumentForm
from django.views.generic import TemplateView,DetailView
from django.views.generic.list import ListView
from accounts.models import MyProfile
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from posts.models import Post
from Msg.models import Message
import os

class doc_list(TemplateView):
    def post(self, request, *args, **kwargs):
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.author = MyProfile.objects.get(user=request.user)
            newdoc.doctypeTag = request.POST['doctypeTag']
            newdoc.schoolnameTag = request.POST['schoolnameTag']
            newdoc.description = request.POST['description']
            newdoc.title = request.POST['title']
            newdoc.save()

            # Redirect to the document list after POST
        return HttpResponseRedirect("/files")
    def get(self, request, *args, **kwargs):
        form = DocumentForm() # A empty, unbound form
        documents = Document.objects.exclude(doctypeTag="private").order_by("-time")
        return render_to_response(
            'file.html',
            {'documents': documents, 'form': form, 'bulletins' : Post.objects.filter(tag1='announcement').order_by("-time")},
            context_instance=RequestContext(request)
        )

class folder_detail(TemplateView):
    template_name = 'folder_detail.html'
    def get(self, request, *args, **kwargs):
        form = DocumentForm() 
        folder = Folder.objects.get(pk=kwargs['pk'])
        subfolders = Folder.objects.filter(upper_folder = kwargs['pk'])
        subfiles = Document.objects.filter(folder = kwargs['pk'])
        return render(request, self.template_name, {'form': form, 'folder':folder, 'subfolders': subfolders,'subfiles':subfiles, 'bulletins' : Post.objects.filter(tag1='announcement').order_by("-time")}) 
    def post(self, request, *args, **kwargs):
        
        if 'add_doc' in request.POST:
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                newdoc = Document(docfile = request.FILES['docfile'])
                newdoc.author = MyProfile.objects.get(user=request.user)
                newdoc.description = request.POST['description']
                newdoc.title = request.POST['title']
                newdoc.doctypeTag = "private"
                newdoc.folder = Folder.objects.get(pk=kwargs['pk'])
                newdoc.save()
            return HttpResponseRedirect("/files/myfiles/"+kwargs['pk'])
        elif 'add_folder' in request.POST:
            newfold = Folder(title=request.POST['new_folder_name'])
            newfold.author = MyProfile.objects.get(user=request.user) 
            newfold.upper_folder = Folder.objects.get(pk=kwargs['pk'])
            newfold.save()
            return HttpResponseRedirect("/files/myfiles/"+kwargs['pk'])
        elif 'del_doc' in request.POST:
            msgId = request.POST.get('pri_key', None)
            msgToDel = get_object_or_404(Document, pk = msgId)
            msgToDel.delete()
            return HttpResponseRedirect("/files/myfiles/"+kwargs['pk'])

        elif 'del_folder' in request.POST:
            msgId = request.POST.get('pri_key', None)
            msgToDel = get_object_or_404(Folder, pk = msgId)
            msgToDel.delete()
            return HttpResponseRedirect("/files/myfiles/"+kwargs['pk'])

class ShowFolders(TemplateView):
    template_name = 'folder_list.html'
    def get(self, request, *args, **kwargs):
        form = DocumentForm() 
        folders = Folder.objects.filter(author = request.user).filter(upper_folder__isnull=True)
        bulletins = Post.objects.filter(tag1 = 'announcement').order_by("-time")
        subfiles = Document.objects.filter(folder__isnull =True)
        return render(request, self.template_name, {'subfiles':subfiles,'form': form,'folders': folders, 'bulletins' : bulletins})
    def post(self, request, *args, **kwargs):
        if 'add_doc' in request.POST:
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                newdoc = Document(docfile = request.FILES['docfile'])
                newdoc.author = MyProfile.objects.get(user=request.user)
                newdoc.description = request.POST['description']
                newdoc.title = request.POST['title']
                newdoc.doctypeTag = "private"
                newdoc.save()
            return HttpResponseRedirect("/files/myfiles/")

        elif 'add_folder' in request.POST:
            newfold = Folder(title=request.POST['new_folder_name'])
            newfold.author = MyProfile.objects.get(user=request.user) 
            newfold.save()
            return HttpResponseRedirect("/files/myfiles/")

        elif 'del_doc' in request.POST:
            msgId = request.POST.get('pri_key', None)
            msgToDel = get_object_or_404(Document, pk = msgId)
            msgToDel.delete()
            return HttpResponseRedirect("/files/myfiles/")

        elif 'del_folder' in request.POST:
            msgId = request.POST.get('pri_key', None)
            msgToDel = get_object_or_404(Folder, pk = msgId)
            msgToDel.delete()
            return HttpResponseRedirect("/files/myfiles/")

class ShowFile(ListView):
    model = Document

class FileDetail(DetailView):
    model = Document
    template_name = 'file_detail.html'
    def get(self, request, *args, **kwargs):
        if not request.user.has_perm('accounts.view_profile'):
            return render(request, '401.html')
        document = Document.objects.get(pk=kwargs['pk'])
        allmsg = Message.objects.filter(belong_doc=document).order_by("-time")
        return render(request, self.template_name, {'document':document, 'allmsg': allmsg, 'bulletins' : Post.objects.filter(tag1='announcement').order_by("-time")}) 

    def post(self, request, *args, **kwargs):
        if not request.user.has_perm('accounts.view_profile'):
            return render(request, '401.html')
        newmsg = Message()
        newmsg.context = request.POST['context']
        newmsg.author = MyProfile.objects.get(user=request.user)
        newmsg.belong_doc = Document.objects.get(pk=request.POST['document_id'])
        newmsg.save()
        return redirect("/files/"+request.POST['document_id'])

    


class PastPostFile(ListView):
    template_name = 'pastpost_file.html'  
    def get(self, request, *args, **kwargs):
        if not request.user.has_perm('accounts.view_profile'):
            return render(request, '401.html')
        newdoc = Document.objects.filter(author = request.user).order_by("-time")
        bulletins = Post.objects.filter(tag1 = 'announcement').order_by("-time")
        return render(request, self.template_name, {'documents': newdoc, 'bulletins' : bulletins})
    def post(self, request, *args, **kwargs):
        if not request.user.has_perm('accounts.view_profile'):
            return render(request, '401.html')
        docId = request.POST.get('file', None)
        docToDel = get_object_or_404(Document, pk = docId)
        docToDel.docfile.delete()
        docToDel.delete()
        return redirect("/pastpost_file")

class MyDocsView(TemplateView):
    template_name = 'mydocs.html'
    def get_context_data(self, **kwargs):
        context = super(MyDocsView, self).get_context_data(**kwargs)
        context['bulletins'] = bulletins = Post.objects.filter(tag1='announcement').order_by("-time")
        return context


class MyFileView(TemplateView):
    template_name = 'myfiles.html'
    def get_context_data(self, **kwargs):
        context = super(MyFileView, self).get_context_data(**kwargs)
        context['bulletins'] = bulletins = Post.objects.filter(tag1='announcement').order_by("-time")
        return context


