from django.db import models

# Create your models here.
from django.contrib.auth.models import User  
from django.utils.translation import ugettext as _  
from userena.models import UserenaBaseProfile # or UserenaLanguageBaseProfile
  
class Category(models.Model):
	name = models.CharField(max_length=30, blank=True)
	description = models.CharField(max_length=30, blank=True) 
	def __unicode__(self):
		return self.name

class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User) 
    description = models.CharField(_('description'),max_length=30) 
    school = models.CharField(max_length=30)       
    phone_number = models.CharField(max_length=30) 
    category = models.ForeignKey(Category, blank=True, null=True)
    name =  models.CharField(max_length=30)   


