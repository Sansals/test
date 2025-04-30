import django.contrib.auth.views
from django.urls import path, reverse_lazy
from . import views
from . import services
from django.contrib.auth.views import *
from .forms import MyPasswordResetForm,MySetPasswordForm

app_name = 'users'

urlpatterns = [
    path('login/', views.auth_view, name="login"),
    path('registration/', views.registration_view, name='reg'),
    path('logout/', services.logout_user ,name='logout' ),
    path('registration/vrmail/', views.email_verification_view, name='vrmail'),
    path('registration/vrmail1/', services.verification_email, name='verification_email'),

    path('password-reset/',
         PasswordResetView.as_view(template_name='password_reset/password_reset_form.html',
                                   email_template_name = 'password_reset/password_reset_email.html',
                                    form_class = MyPasswordResetForm ,
                                   success_url=reverse_lazy('users:password_reset_done')),
         name='password_reset'),
    path('password-reset/done/',
         PasswordResetDoneView.as_view(template_name='password_reset/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='password_reset/password_reset_confirm.html',
                                          form_class = MySetPasswordForm ,
                                          success_url=reverse_lazy('users:password_reset_complete')),
         name='password_reset_confirm'),
    path('password-reset/complete/',
         PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
         name='password_reset_complete')
]