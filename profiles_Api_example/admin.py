from django.contrib import admin
from profiles_Api_example import models
# Register your models here.

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)