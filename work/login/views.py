from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from work.global_services import get_username, get_user_email, get_user, get_user_verify_is
from shop.services import basket_value
from .services import save_verify_code, verification_email, get_session_data, set_user_verify_true, \
    registration_user_save

from .forms import AuthForm, UserRegistrationForm, VrMail


def email_verification_view(request):
    """Представление формы верификации адреса эл. почты"""
    error=''
    form = VrMail
    if request.method == "POST":
        form = VrMail(request.POST)
        if form.is_valid():
            code = get_session_data(request, session_name='sessiondata', name='code')
            if int(form.cleaned_data['ver_mail']) == code:
                set_user_verify_true(request)
                return redirect('home')
        else:
            error = f'{get_username(request)}, введите коректный код!'
    data={
        'form': form,
        'error': error,
        'username': get_username(request),
        'email': get_user_email(request),
        'basket_value': basket_value(request),
    }
    return render(request, 'auth/vermail.html', data)



def auth_view(request):
    """Представление формы авторизации пользователей"""
    error=''

    user = AuthForm(data=request.POST or None)

    if request.method == "POST":
        if user.is_valid():
            username = user.cleaned_data['username']
            password = user.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user:
                login(request, user)
                if get_user_verify_is(request) == True:
                    return redirect('home')
                else:
                    return redirect('users:verification_email')
            else:
                error = 'Пользователя не существует'
        else:
            error = 'Пользователь не существует'



    data = {
        'authform': user,
        'error': error,
    }
    return render(request, 'auth/auth.html', data)


def registration_view(request):
    if not request.user.is_authenticated:
        error_tag=''
        form = UserRegistrationForm(data= request.POST or None)
        if request.method == "POST":
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                registration_user_save(request, form)
                save_verify_code(request)
                return redirect('users:vrmail')
    else:
        return redirect('home')

    data = {
        'form':form,
    }
    return render(request, 'auth/reg.html', data)
# Create your views here.