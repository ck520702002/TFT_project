# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import os

#each folder has a title and an author
class Folder(models.Model):
	title = models.CharField(max_length=20,blank=False)
	author = models.ForeignKey("accounts.MyProfile")
	upper_folder = models.ForeignKey("Folder",null=True,blank=True)
	def __unicode__(self):
		return self.title

#each docuemnt has a set of 
class Document(models.Model):
	title = models.CharField(max_length=20,blank=True)
	description = models.CharField(max_length=200,blank=True)
	docfile = models.FileField(upload_to='documents/%Y/%m/%d')
	time = models.DateTimeField(auto_now = True)
	author = models.ForeignKey("accounts.MyProfile")
	doctypeTag = models.CharField(max_length=10,blank=True)
	schoolnameTag = models.CharField(max_length=10,blank=True)
	folder = models.ForeignKey("Folder",blank=True,null=True)
	def __unicode__(self):
		return self.title