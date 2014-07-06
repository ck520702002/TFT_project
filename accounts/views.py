from django.shortcuts import render
from django.views.generic.simple import direct_to_template
from django.http import Http404

# Create your views here.
def teacher(request, page_name):
    # Use some exception handling, just to be safe
    try:
        return direct_to_template(request, '%s.html' % (page_name, ))
    except TemplateDoesNotExist:
        raise Http404