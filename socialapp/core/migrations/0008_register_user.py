# Generated by Django 2.2.3 on 2019-07-05 09:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_register_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='friend_requests',
            field=models.ManyToManyField(blank=True, related_name='friend_requests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='friends', to=settings.AUTH_USER_MODEL),
        ),
    ]
