from random import randint

from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from work.global_services import get_username, get_user_email, get_user_verify_is

from .forms import VrMail
from .models import User_Status

def email_verification_form(request):
    form = VrMail
    if request.method == "POST":
        form = VrMail(request.POST)
        if form.is_valid():
            if int(form.cleaned_data['ver_mail']) == int(_get_session_data(request, name='code')):
                _set_user_verify_true(request)
                return redirect('home')
            else:
                request.session['sessiondata'] = request.session.pop('sessiondata', {})
                error = f'{get_username(request)}, введите коректный код!'
        else:
            error = f'{get_username(request)}, введите коректный код!'
    return form

def logout_user(request):
    logout(request)
    return redirect(request.META['HTTP_REFERER'])

def set_user_verify_true(request):
    try:
        u = User_Status.objects.get(username=request.user.id)
        u.Isverified = True
        u.save()
        #logging
    except:
        pass #logging

def get_session_data(request, name):
    data = request.session.pop('sessiondata', {})
    try:
        return data.get(name)
    except AttributeError:
        return 79797979
        #logging ошибка получения сессионных данных, превышено кол-во запросов
    except Exception:
        return 79797979
        # logging Не известная ошибка получения сессионных данных

def registration_user_save(request, form):
    """Сохраняет и авторизирует нового пользователя, создаёт для него расширение модели User"""
    user = form.save(commit=False)
    user.set_password(form.cleaned_data['password'])
    user.save()
    login(request, authenticate(username=user.username, password=form.cleaned_data['password']))
    _create_status_object_for_registration_user(request)

def save_verify_code(request):
    data = {
        'code': _send_verify_code(request)
    }
    request.session['sessiondata'] = data

def _create_status_object_for_registration_user(request):
    u = User.objects.get(username=request.user.username)
    User_Status.objects.create(username=u)

def _send_verify_code(request):
    """Генерирует и отправляет код для подтверждения эл. почты"""
    try:
        code = randint(100000, 999999)
        send_mail(
            'Подтверждение учётной записи',
            f'Уважаемый {get_username(request)}, Ваш код для подтверждения учётной записи по адресу электронной почты: {code}',
            'stereotip.228@gmail.com',
            [get_user_email(request)],
            fail_silently=False
        )
        # logging
    except:
        pass #logging
    return code