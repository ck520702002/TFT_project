from django.db import models
from django.contrib.auth.models import User  
# Create your models here.
class Announcement (models.Model):
	"""docstring for Announcement:"""

	title = models.CharField(max_length=1000)
	context = models.CharField(max_length=100000)
	time = models.DateTimeField(auto_now = True)
	author = models.ForeignKey(User, blank=True, null=True)
	
	def __unicode__(self):
		return self.title