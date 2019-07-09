from django.conf.urls import url

from . import views
from django.urls import path
from .views import EditProfileView, PostsPage, PostDetailPage, EditPost
from .views import UserProfilePage, RegisterPage

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<int:pk>/', UserProfilePage.as_view(), name='user_profile_page_view'),
    path('posts/', PostsPage.as_view(), name='posts'),
    path('posts/<int:pk>', PostDetailPage.as_view(), name='post_detail_page_view'),
    path('posts/<int:post_id>/edit', EditPost.as_view(), name='edit_post'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('profile/<int:user_id>/edit/', EditProfileView.as_view(), name='edit_profile'),
]
