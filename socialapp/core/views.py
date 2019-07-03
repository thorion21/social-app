from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from .models import Post, Comment

User = get_user_model()


# Create your views here.


def index(request):
    return HttpResponse('I think it works...')


def posts_page(request):
    posts = Post.objects.all()

    return render(request, 'posts.html',
                  {'posts': posts})


def user_profile_page(request, user_id):
    try:
        current_user = User.objects.get(pk=user_id)
    except ObjectDoesNotExist:
        error_string = "User not found"
        return render(request, 'error_page.html', {'text': error_string})

    return render(request, 'user_profile.html', {'user': current_user})


