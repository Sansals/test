from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, Form
from django import forms



class VrMail(Form):
    ver_mail = forms.IntegerField(widget=forms.TextInput(attrs={
        'class':'input-field',
        'placeholder': 'Введите код',
        'id':'ver_mail'
    }))


class AuthForm(AuthenticationForm):
    """Форма авторизации"""
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'input-field',
        'placeholder': 'Логин',
        'id': 'username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'input-field',
        'placeholder': 'Пароль',
        'id': 'password'
    }))


class UserRegistrationForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'input-field',
        'placeholder': 'Повтор пароля',
        'id': 'confirm-password'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']

        widgets = {
            'username': TextInput(attrs={
                'class': 'input-field',
                'placeholder': 'Введите логин',
                'id': 'username',
            }),
            'email': TextInput(attrs={
                'class': 'input-field',
                'placeholder': 'Введите почту',
                'id': 'email',
            }),
            'password': TextInput(attrs={
                'class': 'input-field',
                'type':'password',
                'placeholder': 'Пароль',
                'id': 'password',
            })

        }