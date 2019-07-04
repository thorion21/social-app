from django.conf.urls import url

from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<int:user_id>/',views.user_profile_page, name='user_profile_page_view'),
    path('posts/', views.posts_page, name='posts'),
    path('register/', views.register_page, name='register')

]
git
