# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from filesManagement.models import Document
from filesManagement.forms import DocumentForm
from django.views.generic.list import ListView
from accounts.models import MyProfile
import os
def list(request):
    # Handle file upload
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
    for document in documents:
        document.docfile.name = os.path.basename(document.docfile.name)
        #documents.insert(0, document)
    #for document in testdocs:
    #    document.docfile.name = os.path.basename(document.docfile.name)

    #for document in documents:
    #    document.docfile.name = os.path.basename(document.docfile.name)

    # Render list page with the documents and the form
    return render_to_response(
        'file.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

class ShowFile(ListView):
    template_name = 'files.html'    
