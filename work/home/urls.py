from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('rules/', views.rules_view, name="rules"),
    path('news/', views.news_view, name="news"),
]