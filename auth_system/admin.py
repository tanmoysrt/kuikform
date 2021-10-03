from django.contrib import admin
from auth_system.models import UserProfile, APIToken

admin.site.register(UserProfile)
admin.site.register(APIToken)
