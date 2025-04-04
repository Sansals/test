from django.contrib import admin
from django.urls import path, include
from . import views
from . import services

urlpatterns = [
    path('', views.all_profiles_view, name="profiles"),
    path('<str:url_username>/', views.user_profile_view, name='profile'),
    path('profile/avatar-update/<int:pk>/', services.AvatarUpdateView.as_view(), name='update_avatar'),
]