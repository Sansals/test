from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('rules/', views.rules_view, name="rules"),
    path('news/', views.news_view, name="news"),
    path('new/<int:id>', views.new_article_view, name="new_view"),
    path('new/error_404', views.new_article_not_founded, name="new_not_founded"),
]