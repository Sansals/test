from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, Form
from django import forms
from django.contrib.auth.forms import PasswordResetForm,SetPasswordForm
import re

class MySetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(MySetPasswordForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'border-2 rounded-xl text-black text-lg px-2 py-1'

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email",
                                       'class': 'border-2 rounded-xl text-black text-lg px-2 py-1',
                                       'placeholder': 'Введите Email'
                                       }),
    )


class VrMail(Form):
    ver_mail = forms.IntegerField(widget=forms.TextInput(attrs={
        'class':'w-full rounded-md border-1 border-black p-2',
        'placeholder': 'Введите код',
        'id':'ver_mail'
    }))


class AuthForm(AuthenticationForm):
    """Форма авторизации"""
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'w-full rounded-md border-1 border-black p-2',
        'placeholder': 'Логин',
        'id': 'username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'w-full rounded-md border-1 border-black p-2',
        'placeholder': 'Пароль',
        'id': 'password'
    }))


class UserRegistrationForm(forms.ModelForm):

    error_messages = {
        'email_is_busy': 'Данный адрес электронной почты уже зарегистрирован',
        'passwords_dont_match': 'Пароли не совпадают',
        'email_short': 'Длинна данного поля не менее 8 символов',
        'password_short': 'Длинна данного поля не менее 8 символов',
        'username_uncorrected': 'Имя пользователя может содержать только символы A-Z, a-z, 0-9 !',

    }

    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'w-full rounded-md border-1 border-black p-2',
        'placeholder': 'Повтор пароля',
        'id': 'confirm-password'
    }))

    tag = forms.BooleanField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']

        widgets = {
            'username': TextInput(attrs={
                'class': 'w-full rounded-md border-1 border-black p-2',
                'placeholder': 'Введите логин',
                'id': 'username',
            }),
            'email': TextInput(attrs={
                'class': 'w-full rounded-md border-1 border-black p-2',
                'placeholder': 'Введите почту',
                'id': 'email',
            }),
            'password': TextInput(attrs={
                'class': 'w-full rounded-md border-1 border-black p-2',
                'type':'password',
                'placeholder': 'Пароль',
                'id': 'password',
            })

        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        if username:
            regex = "^[a-zA-Z0-9]+$"
            pattern = re.compile(regex)
            if pattern.search(username):
                pass
            else:
                raise forms.ValidationError(self.error_messages['username_uncorrected'], code='username_uncorrected')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            user = 0
            try:
                user = User.objects.get(email=email)
            except Exception:
                pass
            if user !=0:
                raise forms.ValidationError(self.error_messages['email_is_busy'], code='email_is_busy')
        return email

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm:
            if password != password_confirm:
                raise forms.ValidationError(self.error_messages['passwords_dont_match'], code='passwords_dont_match')
        return password_confirm

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            if len(password) < 8:
                raise forms.ValidationError(self.error_messages['password_short'], code='password_short')
        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            if len(email) < 8:
                raise forms.ValidationError(self.error_messages['email_short'], code='email_short')
        return email
