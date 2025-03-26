
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_news_view, name="createnews"),
    path('<int:pk>/', views.NewsDatailView.as_view(), name='news-detail')
]