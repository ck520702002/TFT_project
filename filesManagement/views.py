# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from filesManagement.models import Document, Folder
from filesManagement.forms import DocumentForm
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from accounts.models import MyProfile
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from posts.models import Post
import os

def doc_list(request):
    # Handle file upload
    if not request.user.has_perm('accounts.view_profile'):
            return render(request, '401.html')
    if request.method == 'POST':
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
            return HttpResponseRedirect(reverse('filesManagement.views.doc_list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all().order_by("-time")
    #for document in documents:
        #document.docfile.name = os.path.basename(document.docfile.name)

    # Render list page with the documents and the form
    return render_to_response(
        'file.html',
        {'documents': documents, 'form': form, 'bulletins' : Post.objects.filter(tag1='announcement').order_by("-time")},
        context_instance=RequestContext(request)
    )

class ShowFolders(TemplateView):
    template_name = 'folder_list.html'
    def get(self, request, *args, **kwargs):
        if not request.user.has_perm('accounts.view_profile'):
            return render(request, '401.html')
        folders = Folder.objects.filter(author = request.user)
        bulletins = Post.objects.filter(tag1 = 'announcement').order_by("-time")
        import pdb;pdb.set_trace();
        return render(request, self.template_name, {'folders': folders, 'bulletins' : bulletins})  

class ShowFile(ListView):
    model = Document

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


