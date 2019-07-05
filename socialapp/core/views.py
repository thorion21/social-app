from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from .models import Post, Comment, UserProfile
from .forms import PostForm, UserForm

User = get_user_model()


# Create your views here.


def index(request):
    return HttpResponse('I think it works...')


def posts_page(request):

    if request.method == 'GET':
        posts = Post.objects.all()
        form = PostForm()

        return render(request, 'posts.html',
                      {'posts': posts, 'form': form})

    form = PostForm(request.POST)

    if form.is_valid():
        text = form.cleaned_data['text']
        s = Post(text=text, created_by=request.user)
        s.save()

        form = PostForm()
        posts = Post.objects.all()

        return render(request, 'posts.html',
                      {'posts': posts, 'form': form})


def user_profile_page(request, user_id):
    try:
        current_user = User.objects.get(pk=user_id)
    except ObjectDoesNotExist:
        error_string = "User not found"
        return render(request, 'error_page.html', {'text': error_string})

    return render(request, 'user_profile.html', {'user': current_user})


def register_page(request):

    if request.method == 'GET':
        form = UserForm()

        return render(request, 'register_page.html',
                      {'form': form})

    form = UserForm(request.POST)

    if form.is_valid():
        data = form.cleaned_data\

        username = data['username']
        email = data['email']
        password = data['password']

        extra_args = {
            'first_name': data['first_name'],
            'last_name': data['last_name']
        }
        new_user = User.objects.create_user(username=username, email=email, password=password, **extra_args)

        new_user_profile = UserProfile(user=new_user)
        new_user_profile.save()

        return render(request, 'user_profile.html',
                      {'user': new_user})

    return render(request, 'error_page.html',
                  {'text': "Error occurred during registration"})



