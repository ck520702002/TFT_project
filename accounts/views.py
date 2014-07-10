from django.shortcuts import render
from accounts import forms
from userena import views as userena_views
#from django.views.generic.edit import CreateView

# Create your views here.


def profile_edit(request, username, edit_profile_form=forms.CustomEditProfileForm,
                 template_name='userena/profile_form.html', success_url=None,
                 extra_context=None, **kwargs):
    
    return userena_views.profile_edit(request=request, username=username,
            edit_profile_form=edit_profile_form, template_name=template_name,
            success_url=success_url, extra_context=extra_context)
