from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.shopview, name="shop"),
    path('basket/', views.basket, name='basket'),
    path('basket/basket_add/<slug:product_slug>/', views.basket_add, name='basket_add'),
    path('basket/basket_change/<slug:product_slug>/', views.basket_change, name='basket_change'),
    path('basket/basket_remove/<slug:product_slug>/', views.basket_remove, name='basket_remove'),
]