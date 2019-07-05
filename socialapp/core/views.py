from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from .models import Post, Comment, UserProfile
from .forms import PostForm, UserForm, CommentForm
from django.contrib import messages

User = get_user_model()


# Create your views here.


def index(request):
    return HttpResponse('I think it works...')


def posts_page(request):
    posts = Post.objects.all()
    if request.method == 'GET':
        return render(request, 'posts.html',
                      {'posts': posts, 'form': PostForm()})

    form = PostForm(request.POST)

    if form.is_valid():
        text = form.cleaned_data['text']
        new_post = Post(text=text, created_by=request.user)
        new_post.save()

        return render(request, 'posts.html',
                      {'posts': posts, 'form': PostForm()})


def post_detail_page(request, post_id):

    try:
        current_post = Post.objects.get(pk=post_id)
    except ObjectDoesNotExist:
        error_string = "Post not found"
        return render(request, 'error_page.html', {'text': error_string})

    if request.method == 'GET':
        return render(request, 'post_details.html',
                      {
                          'post': current_post,
                          'form': CommentForm(),
                          'edit_form': PostForm(),
                          'request_user': request.user
                      })

    form = CommentForm(request.POST)

    if form.is_valid():
        text = form.cleaned_data['text']
        new_comment = Comment(text=text, created_by=request.user, post=current_post)
        new_comment.save()

        return redirect('post_detail_page_view', post_id=post_id)


def edit_post(request, post_id):
    post_to_update = Post.objects.get(pk=post_id)
    form = PostForm(request.POST)

    if form.is_valid():
        text = form.cleaned_data['text']
        post_to_update.text = text
        post_to_update.save()

    return redirect('post_detail_page_view', post_id=post_id)


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
        data = form.cleaned_data

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
