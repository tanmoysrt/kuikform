import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from auth_system.manager import CustomUserManager


class UserProfile(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    username = None
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True)
    picture = models.FileField(upload_to="profile_pics",default="default_profile_pic.jpeg")
    verified = models.BooleanField(default=False)
    user_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    REQUIRED_FIELDS = ["first_name","last_name"]
    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    def __str__(self):
        return str(self.id)


class APIToken(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="api_token")
    token = models.TextField(null=True, unique=True)
    generated_on = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(max_length=150, null=True)

