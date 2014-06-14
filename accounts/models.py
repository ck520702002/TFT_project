from django.db import models

# Create your models here.
from django.contrib.auth.models import User  
from django.utils.translation import ugettext as _  
from userena.models import UserenaBaseProfile # or UserenaLanguageBaseProfile
  
class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User) 
    description = models.CharField(_('description'),max_length=30) 
    school = models.CharField(max_length=30)       
    phone_number = models.CharField(max_length=30) 
    account = models.CharField(max_length=30)  
    password =  models.CharField(max_length=30)      


