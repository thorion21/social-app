from django.conf.urls import url

from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<int:user_id>/', views.user_profile_page, name='user_profile_page_view'),
    path('posts/', views.posts_page, name='posts'),
    path('posts/<int:post_id>', views.post_detail_page, name='post_detail_page_view'),
    path('register/', views.register_page, name='register')
]
