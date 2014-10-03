# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from filesManagement.models import Document
from filesManagement.forms import DocumentForm
from django.views.generic.list import ListView
from accounts.models import MyProfile
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from posts.models import Post
import os

def list(request):
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
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('filesManagement.views.list'))
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

class ShowFolders(ListView):
    template_name = 'myfolders.html'

class ShowFile(ListView):
    template_name = 'files.html'  

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


