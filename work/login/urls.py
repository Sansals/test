from django.urls import path
from . import views
from . import services

urlpatterns = [
    path('login/', views.auth_view, name="auth"),
    path('registration/', views.registration_view, name='reg'),
    path('logout/', services.logout_user ,name='logout' ),
    path('registration/vrmail', views.email_verification_view, name='vrmail')
]