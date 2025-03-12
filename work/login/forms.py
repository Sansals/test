from django.contrib.auth.forms import AuthenticationForm
from django import forms

class AuthForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)