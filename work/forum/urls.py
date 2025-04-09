
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.forum_view, name="forum"),
    path('<int:pk>/', views.ArticlesDatailView.as_view(), name='news-detail'),
    path('techsupport/', views.techsupport_form_view, name='techsupport_form')
]