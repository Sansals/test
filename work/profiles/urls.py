from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_profiles_view, name="profiles"),
    path('<str:url_username>/', views.user_profile_view, name='profile'),
    path('profile/avatar-update/<int:pk>/', views.AvatarUpdateView.as_view(), name='update_avatar'),
]