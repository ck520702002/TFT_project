from django.shortcuts import render
from accounts import forms
from userena import views as userena_views
#from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from accounts.models import MyProfile
from django.shortcuts import get_object_or_404
from userena.utils import signin_redirect, get_profile_model, get_user_model
from userena import settings as userena_settings
from posts.models import Post
from userena.forms import EditProfileForm
# Create your views here.
def profile_edit(request, username, edit_profile_form=EditProfileForm,
                 template_name='userena/profile_form.html', success_url=None,
                 extra_context=None, **kwargs):
    def get_context_data(self, **kwargs):
        context = super(MyDocsView, self).get_context_data(**kwargs)
        context['bulletins'] = Post.objects.filter(tag1='announcement').order_by("-time")
        return context

class ProfileView(DetailView):
    def get():
        template_name = 'userena/profile_view.html'
        searchProfile = get_object_or_404(MyProfile, pk = kwargs['pk'])
        import pdb;pdb.set_trace()
        return render(request, self.template_name, {'profile': searchProfile,'bulletins' : Post.objects.filter(tag1='announcement').order_by("-time")})

def profile_detail(request, username,extra_context=None, **kwargs):

    template_name = 'userena/profile_detail.html'
    user = get_object_or_404(get_user_model(),
                             username__iexact=username)
    profile_model = get_profile_model()
    try:
        profile = user.get_profile()
    except profile_model.DoesNotExist:
        profile = profile_model.objects.create(user=user)

    if not profile.can_view_profile(request.user):
        raise PermissionDenied
    return render(request, template_name, {'profile': profile,'bulletins' : Post.objects.filter(tag1='announcement').order_by("-time")})


