from django.contrib import admin
from auth_system.models import UserProfile, APIToken, ResetLinkDirectory, VerifyMailLinkDirectory

admin.site.register(UserProfile)
admin.site.register(APIToken)
admin.site.register(ResetLinkDirectory)
admin.site.register(VerifyMailLinkDirectory)
