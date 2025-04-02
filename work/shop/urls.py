from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.shop_view, name="shop"),
    path('basket/', views.basket_view, name='basket'),
    path('basket/buy/', views.payment_basket, name='payment_basket'),
    path('basket/basket_add/<slug:product_slug>/', views.basket_add, name='basket_add'),
    path('basket/basket_change/<slug:product_slug>/', views.basket_change, name='basket_change'),
    path('basket/basket_remove/<int:product_id>/', views.basket_remove, name='basket_remove'),
]