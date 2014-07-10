from django import forms
from django.utils.translation import ugettext_lazy as _

from userena.forms import SignupForm

class SignupFormExtra(SignupForm):
    """ 
    A form to demonstrate how to add extra fields to the signup form, in this
    case adding the first and last name.
    

    """

    def __init__(self, *args, **kw):
        """
        
        A bit of hackery to get the first name and last name at the top of the
        form instead at the end.
        
        """
        super(SignupFormExtra, self).__init__(*args, **kw)
        # Put the first and last name at the top
        new_order = self.fields.keyOrder[:-2]
        self.fields.keyOrder = new_order

    def save(self):
        """ 
        Override the save method to save the first and last name to the user
        field.

        """
        # First save the parent form and get the user.
        new_user = super(SignupFormExtra, self).save()

        new_user.save()

        # Userena expects to get the new user from this form, so return the new
        # user.
        return new_user
