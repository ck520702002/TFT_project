from django.db import models
import datetime
from django.utils import timezone
import datetime
from accounts.models import MyProfile
from userena.models import UserenaBaseProfile # or UserenaLanguageBaseProfile

class Post(models.Model):

	title = models.CharField(max_length=10)
	context = models.CharField(max_length=500)
	time = datetime.datetime.now()
#	author = models.ForeignKey(MyProfile)
	tag = models.CharField(max_length=500)

	def __unicode__(self):  # Python 3: def __str__(self):
		return  self.title
    
