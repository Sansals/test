
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('create/', views.forum_view, name="createnews"),
    path('<int:pk>/', views.ArticlesDatailView.as_view(), name='news-detail')
]