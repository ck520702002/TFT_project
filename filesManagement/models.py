# -*- coding: utf-8 -*-
from django.db import models

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    time = models.DateTimeField(auto_now = True)
    author = models.ForeignKey("accounts.MyProfile")
    doctypeTag = models.CharField(max_length=10,blank=True)
    schoolnameTag = models.CharField(max_length=10,blank=True)