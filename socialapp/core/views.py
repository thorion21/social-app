from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from .models import Post, Comment, UserProfile, Country
from .forms import PostForm, UserForm, CommentForm, EditProfileForm
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView

User = get_user_model()

# Create your views here.


def index(request):
    return HttpResponse('I think it works...')


class PostsPage(ListView, FormView):
    model = Post
    template_name = "posts.html"
    form_class = PostForm
    success_url = './'

    def form_valid(self, form):
        text = form.cleaned_data['text']
        new_post = Post(text=text, created_by=self.request.user)
        new_post.save()
        return super().form_valid(form)


class PostDetailPage(DetailView):
    model = Post
    template_name = "post_details.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PostDetailPage, self).get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['edit_form'] = PostForm()
        return context

    def post(self, request, pk):
        try:
            current_post = Post.objects.get(pk=pk)
        except ObjectDoesNotExist:
            error_string = "Post not found"
            return render(request, 'error_page.html', {'text': error_string})

        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            new_comment = Comment(text=text, created_by=request.user, post=current_post)
            new_comment.save()

        return redirect('post_detail_page_view', pk=pk)


class EditPost(View):

    def post(self, request, post_id):
        post_to_update = Post.objects.get(pk=post_id)
        form = PostForm(request.POST)

        if form.is_valid():
            text = form.cleaned_data['text']
            post_to_update.text = text
            post_to_update.save()
            return redirect('post_detail_page_view', pk=post_id)


class UserProfilePage(DetailView):
    model = User
    template_name = "user_profile.html"


class RegisterPage(FormView):
    form_class = UserForm
    template_name = "register_page.html"

    def post(self, request):
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

            return redirect('user_profile_page_view', pk=new_user.id)

        return render(request, 'error_page.html',
                  {'text': "Error occurred during registration"})


class EditProfileView(View):

    def get(self, request, user_id):
        try:
            current_user = User.objects.get(pk=user_id)
        except ObjectDoesNotExist:
            error_string = "User not found"
            return render(request, 'error_page.html', {'text': error_string})

        form = EditProfileForm()

        if current_user.user_profiles.birthday:
            birthday = current_user.user_profiles.birthday.strftime("%Y-%m-%d")
        else:
            birthday = None

        return render(request, 'edit_user_profile.html',
                          {'user': current_user, 'form': form, 'birthday': birthday})

    def post(self, request, user_id):
        current_user = User.objects.get(pk=user_id)
        form = EditProfileForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user_update_args = {
                'first_name': data['first_name'],
                'last_name': data['last_name'],
                'email': data['email'],
            }
            user_profile_update_args = {
                'image': data['image'],
                'birthday': data['birthday'],
                'country': Country.objects.filter(name=data['country']).values_list('code', flat=True)[0],
            }
            User.objects.filter(pk=current_user.id).update(**user_update_args)
            current_profile = UserProfile.objects.filter(user=current_user)
            current_profile.update(**user_profile_update_args)

            return redirect('user_profile_page_view', pk=user_id)
