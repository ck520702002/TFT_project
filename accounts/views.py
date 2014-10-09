from django.shortcuts import render
from accounts import forms
from userena import views as userena_views
#from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login, logout, REDIRECT_FIELD_NAME
from accounts.models import MyProfile
from django.shortcuts import get_object_or_404,redirect
from userena.utils import signin_redirect, get_profile_model, get_user_model
from userena.views import ExtraContextTemplateView
from userena import settings as userena_settings
from posts.models import Post
from userena.forms import EditProfileForm,SignupForm
from userena import signals as userena_signals
from .models import MyProfile
# Create your views here.
def profile_edit(request, username, edit_profile_form=EditProfileForm,
                 template_name='userena/profile_form.html', success_url=None,
                 extra_context=None, **kwargs):
    user = get_object_or_404(get_user_model(),
                             username__iexact=username)

    profile = user.get_profile()

    user_initial = {'first_name': user.first_name,
                    'last_name': user.last_name}

    form = edit_profile_form(instance=profile, initial=user_initial)

    if request.method == 'POST':
        form = edit_profile_form(request.POST, request.FILES, instance=profile,
                                 initial=user_initial)

        if form.is_valid():
            profile = form.save()

            if userena_settings.USERENA_USE_MESSAGES:
                messages.success(request, _('Your profile has been updated.'),
                                 fail_silently=True)

            if success_url:
                # Send a signal that the profile has changed
                userena_signals.profile_change.send(sender=None,
                                                    user=user)
                redirect_to = success_url
            else: redirect_to = reverse('userena_profile_detail', kwargs={'username': username})
            return redirect(redirect_to)

    if not extra_context: extra_context = dict()
    extra_context['form'] = form
    extra_context['profile'] = profile
    extra_context['bulletins'] = Post.objects.filter(tag1='announcement').order_by("-time")
    return render(request, template_name, extra_context)

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

def signup(request, signup_form=SignupForm,
           template_name='userena/signup_form.html', success_url=None,
           extra_context=None):
    # If signup is disabled, return 403
    if userena_settings.USERENA_DISABLE_SIGNUP:
        raise PermissionDenied

    # If no usernames are wanted and the default form is used, fallback to the
    # default form that doesn't display to enter the username.
    if userena_settings.USERENA_WITHOUT_USERNAMES and (signup_form == SignupForm):
        signup_form = SignupFormOnlyEmail

    form = signup_form()

    if request.method == 'POST':
        form = signup_form(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            new_profile = MyProfile(user=user)
            # Send the signup complete signal
            userena_signals.signup_complete.send(sender=None,
                                                 user=user)


            if success_url: redirect_to = success_url
            else: redirect_to = reverse('userena_signup_complete',
                                        kwargs={'username': user.username})

            # A new signed user should logout the old one.
            if request.user.is_authenticated():
                logout(request)

            if (userena_settings.USERENA_SIGNIN_AFTER_SIGNUP and
                not userena_settings.USERENA_ACTIVATION_REQUIRED):
                user = authenticate(identification=user.email, check_password=False)
                login(request, user)

            return redirect(redirect_to)

    if not extra_context: extra_context = dict()
    extra_context['form'] = form
    return ExtraContextTemplateView.as_view(template_name=template_name,
                                            extra_context=extra_context)(request)
