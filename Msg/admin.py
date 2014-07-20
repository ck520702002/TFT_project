from django.contrib import admin
from Msg.models import Message
from Msg.models import Bulletin
# Register your models here.
admin.site.register(Message)
admin.site.register(Bulletin)