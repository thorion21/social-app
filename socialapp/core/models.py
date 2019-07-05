from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Country(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    birthday = models.DateField(blank=True, null=True)
    image = models.CharField(blank=True, default='', max_length=50)
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='user_profiles',
    )
    friends = models.ManyToManyField(User, related_name="friends", blank=True)
    friend_requests = models.ManyToManyField(User, related_name="friend_requests",
                                             blank=True)

    def __str__(self):
        return 'User ' + self.user.username + ' from ' + self.country.name


class Post(models.Model):
    text = models.CharField(max_length=200)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return 'Post ' + self.text + ' created on ' + self.created_at.strftime('%m/%d/%Y, %H:%M:%S')


class Comment(models.Model):
    text = models.CharField(max_length=75)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return 'Comment ' + self.text + ' created on ' + self.created_at.strftime('%m/%d/%Y, %H:%M:%S')


