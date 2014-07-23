# encoding: utf-8

from django.db import models
from django import forms

# Create your models here.
from django.contrib.auth.models import User ,Group
from django.utils.translation import ugettext as _  
from userena.models import UserenaBaseProfile # or UserenaLanguageBaseProfile


class TFTGroup(models.Model):
    name = models.CharField(max_length=100)
    group = models.OneToOneField(Group)
    def __str__(self):
    	return self.name

class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User) 
    #email = models.EmailField(max_length=40)
    phone_number = models.CharField(max_length=30) 
    school = models.CharField(max_length=30)       
    description = models.CharField(_('description'),max_length=30) 
    authorized_groups = models.ForeignKey("TFTGroup", blank=True, null=True)
    #name =  models.CharField(max_length=30) 
