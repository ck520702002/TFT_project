from django.db import models
import datetime
from django.utils import timezone
import datetime

class Post(models.Model):

	title = models.CharField(max_length=10)
	context = models.CharField(max_length=500)
	time = datetime.datetime.now()
	tag1 = models.CharField(max_length=10,blank=True)
	tag2 = models.CharField(max_length=10,blank=True)
	tag3 = models.CharField(max_length=10,blank=True)

	def __unicode__(self):  # Python 3: def __str__(self):
		return  self.title

class Reply(models.Model):

	post = models.ForeignKey(Post)
	context = models.CharField(max_length=500)
	time = datetime.datetime.now()

	def __unicode__(self):  # Python 3: def __str__(self):
		return  self.title