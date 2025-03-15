from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth, name="auth"),
    path('registration/', views.registration, name='reg'),
    path('logout/', views.logout_view ,name='logout' ),
    path('registration/vrmail', views.email_verification, name='vrmail')
]