import datetime
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Post(models.Model):
    text = models.CharField(max_length=200)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='post_creator'
    )
    created_at = models.DateField(default=datetime.datetime.now)
    updated_at = models.DateField()

    def __str__(self):
        return 'Post', self.text, 'created on', self.created_at.strftime('%m/%d/%Y, %H:%M:%S')


class Comment(models.Model):
    text = models.CharField(max_length=75)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='post_source'
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comment_creator'
    )
    created_at = models.DateField(default=datetime.datetime.now)
    updated_at = models.DateField()

    def __str__(self):
        return 'Comment', self.text, 'created on', self.created_at.strftime('%m/%d/%Y, %H:%M:%S')


class Country(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
