from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from .models import Post, Comment, UserProfile
from .forms import PostForm

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




