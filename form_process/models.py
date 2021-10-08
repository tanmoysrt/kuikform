import uuid

from django.db import models
from auth_system.models import UserProfile as UserProfileModel
from form_process.types import USER_FORM_ACCESS_LEVELS


class Form(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=255, null=True)
    whitelist_mode = models.BooleanField(null=True, default=False)
    whitelist_websites = models.JSONField(null=True, default=list, blank=True)
    variables = models.JSONField(null=True, default=list, blank=True)
    is_active = models.BooleanField(null=True, default=True)
    created_on = models.DateTimeField(auto_now_add=True)


class FormAccess(models.Model):
    user = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE, related_name="user_accesses")
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name="form_accesses")
    access_level = models.CharField(max_length=50, choices=USER_FORM_ACCESS_LEVELS, default="read", null=True)


class FormResponse(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name="form_responses")
    data_json = models.JSONField(null=True, default=dict, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
