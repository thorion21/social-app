from django.conf.urls import url

from . import views
from django.urls import path
from .views import EditProfileView, PostsPage

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<int:user_id>/', views.user_profile_page, name='user_profile_page_view'),
    path('posts/', PostsPage.as_view(), name='posts'),
    path('posts/<int:post_id>', views.post_detail_page, name='post_detail_page_view'),
    path('posts/<int:post_id>/edit', views.edit_post, name='edit_post'),
    path('register/', views.register_page, name='register'),
    path('profile/<int:user_id>/edit/', EditProfileView.as_view(), name='edit_profile'),
]
