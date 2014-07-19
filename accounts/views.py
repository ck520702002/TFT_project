from django.shortcuts import render
from accounts import forms
from userena import views as userena_views
#from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from accounts.models import MyProfile
from django.shortcuts import get_object_or_404

# Create your views here.


def profile_edit(request, username, edit_profile_form=forms.CustomEditProfileForm,
                 template_name='userena/profile_form.html', success_url=None,
                 extra_context=None, **kwargs):
    
    return userena_views.profile_edit(request=request, username=username,
            edit_profile_form=edit_profile_form, template_name=template_name,
            success_url=success_url, extra_context=extra_context)

class ProfileView(DetailView):
    template_name = 'userena/profile_view.html'

    def get(self, request, *args, **kwargs):
    	searchProfile = get_object_or_404(MyProfile, pk = kwargs['pk'])
        print searchProfile.phone_number
        return render(request, self.template_name, {'profile': searchProfile})