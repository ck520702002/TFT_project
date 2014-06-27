from django.db import models
import datetime
from django.utils import timezone
<<<<<<< HEAD
import datetime
from accounts.models import MyProfile
from userena.models import UserenaBaseProfile # or UserenaLanguageBaseProfile
=======
>>>>>>> parent of e98f81f... 結合po文與文章列表

class Post(models.Model):

	title = models.CharField(max_length=10)
	context = models.CharField(max_length=500)
<<<<<<< HEAD
	time = datetime.datetime.now()
#	author = models.ForeignKey(MyProfile)
	tag = models.CharField(max_length=500)

=======
	
>>>>>>> parent of e98f81f... 結合po文與文章列表
	def __unicode__(self):  # Python 3: def __str__(self):
		return  self.title
    
