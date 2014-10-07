from django.db import models

# Create your models here.
class Message(models.Model):
    context = models.CharField(max_length=500)
    time = models.DateTimeField(auto_now = True)
    author = models.ForeignKey("accounts.MyProfile")
    belong_post = models.ForeignKey("posts.Post",null=True,blank=True)
    belong_doc = models.ForeignKey("filesManagement.Document",null=True,blank=True)
    #belong_file = models.ForeignKey("filesManagement.Document")

    def __unicode__(self):  # Python 3: def __str__(self):
        return  self.context

