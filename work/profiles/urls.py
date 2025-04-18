from django.contrib import admin
from django.urls import path, include
from . import views
from . import services

urlpatterns = [
    path('', views.all_profiles_view, name="profiles"),
    path('<str:url_username>/', views.user_profile_view, name='profile'),
    path('profile/avatar-update/<int:pk>/', services.AvatarUpdateView.as_view(), name='update_avatar'),
    path('<str:url_username>/answers', views.user_profile_answers_view, name='profile_view_answers'),
    path('<str:url_username>/comments', views.user_profile_comments_view, name='profile_view_comments'),
]