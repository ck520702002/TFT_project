from django.db import models
import datetime
from django.utils import timezone

class Post(models.Model):

	title = models.CharField(max_length=10)
	context = models.CharField(max_length=500)
	
	def __unicode__(self):  # Python 3: def __str__(self):
		return  self.title
    
