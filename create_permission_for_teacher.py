from accounts.models import MyProfile
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from django.conf import settings
settings.configure() 
content_type = ContentType.objects.get_for_model(MyProfile)
permission = Permission.objects.create(codename='can_access',
                                       name='Can Access Website',
                                       content_type=content_type)