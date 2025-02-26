from django.urls import path
from .views import home, profile, create_post, edit_post, delete_post

urlpatterns = [
    path('', home, name='home'),
    path('profile/', profile, name='profile'),
    path('create/', create_post, name='create_post'),
    path('edit/<int:post_id>/', edit_post, name='edit_post'),
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
]
# Compare this snippet from social_media/urls.py:
# from django.contrib import admin