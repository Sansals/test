
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.addlist, name="addlist"),
    path('create/', views.createnews, name="createnews")
]