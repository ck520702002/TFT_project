from django.db import models
import datetime
from django.utils import timezone
import accounts
from userena.utils import signin_redirect, get_profile_model, get_user_model

class Post(models.Model):

	title = models.CharField(max_length=10)
	context = models.CharField(max_length=500)
	#time = datetime.datetime.now()
	time = models.DateTimeField(auto_now = True)
	#only use tag1 now
	tag1 = models.CharField(max_length=10,blank=True)
	tag2 = models.CharField(max_length=10,blank=True)
	tag3 = models.CharField(max_length=10,blank=True)
	author = models.ForeignKey("accounts.MyProfile")
	
	def __unicode__(self):  # Python 3: def __str__(self):
		return  self.title

