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
    error_css_class = "error"
    required_css_class = "required"

    error_messages = {
        'email_is_busy': 'Данный адрес электронной почты уже зарегистрирован',
        'passwords_dont_match': 'Пароли не совпадают',
        'email_short': 'Длинна данного поля не менее 8 символов',
        'password_short': 'Длинна данного поля не менее 8 символов',

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
