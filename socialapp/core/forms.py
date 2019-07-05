from django.forms import ModelForm
from .models import Post, Comment
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['text']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']


class ContactForm(forms.Form):
    image = forms.CharField(max_length=50, required=False)
    birthday = forms.DateField(required=False)
    email = forms.EmailField(required=False)
    country = forms.IntegerField(required=False)
