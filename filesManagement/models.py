# -*- coding: utf-8 -*-
from django.db import models

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    time = models.DateTimeField(auto_now = True)
    author = models.CharField(max_length=10,blank=True)
