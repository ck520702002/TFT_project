# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

from userena.forms import SignupForm
from userena import views as userena_views
from userena.utils import get_profile_model

class CustomEditProfileForm(userena_views.EditProfileForm):
    """ Base form used for fields that are always required """

    class Meta:
        model = get_profile_model()
        exclude = ['last_name', 'user', 'mugshot', 'privacy',  'first_name']
    def __init__(self, *args, **kwargs):
        super(CustomEditProfileForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label or 'email@address.nl'
        self.fields['school'].widget.attrs['placeholder'] = 'ex.台南國小'
        self.fields['first_name'].label = '名'
        self.fields['last_name'].label = '姓'
        self.fields['email'].label = '帳號'
        self.fields['phone_number'].label = '聯絡電話'
        self.fields['school'].label = '服務地區'
        self.fields['description'].label = '簡介'
        self.fields['category'].label = '個人權限'
        

class SignupFormExtra(SignupForm):
    """ 
    A form to demonstrate how to add extra fields to the signup form, in this
    case adding the first and last name.
    

    """
    first_name = forms.CharField(label=_(u'First name'),
                                 max_length=30,
                                 required=False)

    last_name = forms.CharField(label=_(u'Last name'),
                                max_length=30,
                                required=False)

    def __init__(self, *args, **kw):
        """
        
        A bit of hackery to get the first name and last name at the top of the
        form instead at the end.
        
        """
        super(SignupFormExtra, self).__init__(*args, **kw)
        # Put the first and last name at the top
        new_order = self.fields.keyOrder[:-2]
        new_order.insert(0, 'first_name')
        new_order.insert(1, 'last_name')
        self.fields.keyOrder = new_order

    def save(self):
        """ 
        Override the save method to save the first and last name to the user
        field.

        """
        # First save the parent form and get the user.
        new_user = super(SignupFormExtra, self).save()

        new_user.first_name = self.cleaned_data['first_name']
        new_user.last_name = self.cleaned_data['last_name']
        new_user.save()

        # Userena expects to get the new user from this form, so return the new
        # user.
        return new_user
