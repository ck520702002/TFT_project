from django.contrib import admin
from accounts.models import MyProfile,TFTGroup
# Register your models here.
admin.site.register(TFTGroup)
admin.site.unregister(MyProfile)
admin.site.register(MyProfile)