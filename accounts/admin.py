from django.contrib import admin
from accounts.models import MyProfile
from accounts.models import Category
# Register your models here.
admin.site.register(Category)
admin.site.unregister(MyProfile)
admin.site.register(MyProfile)