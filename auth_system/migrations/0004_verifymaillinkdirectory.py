# Generated by Django 3.2.6 on 2021-10-10 22:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('auth_system', '0003_auto_20211010_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerifyMailLinkDirectory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('verification_key', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verify_mail_link', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
