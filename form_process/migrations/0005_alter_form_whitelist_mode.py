# Generated by Django 3.2.7 on 2021-10-08 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_process', '0004_form_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='whitelist_mode',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
