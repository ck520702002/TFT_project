from django.db import models

# Create your models here.
class Message(models.Model):
    context = models.CharField(max_length=500)
    time = models.DateTimeField(auto_now = True)
    author = models.ForeignKey("accounts.MyProfile")
    belong_post = models.ForeignKey("posts.Post")
    #belong_file = models.ForeignKey("filesManagement.Document")

    def __unicode__(self):  # Python 3: def __str__(self):
        return  self.context


class Bulletin(models.Model):
    title = models.CharField(max_length=50)
    context = models.CharField(max_length=500)
    time = models.DateTimeField(auto_now = True)
    info_url = models.URLField(max_length=500)
    author = models.ForeignKey("accounts.MyProfile")
    def __unicode__(self):  # Python 3: def __str__(self):
        return  self.title