from django.contrib.auth.models import User
from random import randint
from django.conf import settings

from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from work.global_services import get_username, get_user_email, get_user_verify_is

from .forms import VrMail
from .models import User_Status
import datetime
import logging

logger = logging.getLogger(__name__)

def email_verification_form(request):
    form = VrMail
    if request.method == "POST":
        form = VrMail(request.POST)
        if form.is_valid():
            if int(form.cleaned_data['ver_mail']) == int(get_session_data(request, session_name='sessiondata', name='code')):
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
        user_id = get_session_data(request, session_name='user_id', name='user_id')
        logger.info(
            f'{datetime.datetime.now()} |INFO| '
            f'Username: {get_username(request)} |'
            f' |login.services| '
            f'get_session_data_username = {user_id}!'
            f'settings.BETA_TEST_REGISTRATION_MOD = {settings.BETA_TEST_REGISTRATION_MOD}')
        u = User_Status.objects.get(username=user_id)
        u.Isverified = True
        u.save()
        if settings.BETA_TEST_REGISTRATION_MOD == False:
            data = {
                'user_id': User.objects.get(id=user_id).id
            }
            request.session['user_test_id'] = data
            _set_user_is_active_true(request)
        logger.info(
            f'{datetime.datetime.now()} |INFO| '
            f'Username: {get_username(request)} |'
            f' |login.services| '
            f'User set his verified status is True!')
    except Exception:
        logger.warning(
            f'{datetime.datetime.now()} |WARNING| '
            f'Username: {get_username(request)} |'
            f' |login.services| '
            f'Exception: User cant set his verified status is True!')
        pass

def get_session_data(request,session_name, name):
    data = request.session.pop(session_name, {})
    try:
        return data.get(name)
    except AttributeError:
        logger.warning(
            f'{datetime.datetime.now()} |Warning| '
            f'Username: {get_username(request)} |'
            f' |login.services| '
            f'AttributeError: exceeded the number of requests per session!')
        return 79797979
    except Exception:
        logger.warning(
            f'{datetime.datetime.now()} |Warning| '
            f'Username: {get_username(request)} |'
            f' |login.services| '
            f'Exception: exceeded the number of requests per session!')
        return 79797979

def registration_user_save(request, form):
    """Сохраняет и авторизирует нового пользователя, создаёт для него расширение модели User"""
    try:
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(request, authenticate(username=user.username, password=form.cleaned_data['password']))
        _create_status_object_for_registration_user(request)
    except Exception:
        logger.error(
            f'{datetime.datetime.now()} |ERROR| '
            f'Username: {get_username(request)} |'
            f' |login.services| '
            f'Exceptiion: Failed save new user and create new object in model login.User_Status')

def save_verify_code(request):
    data = {
        'code': _send_verify_code(request)
    }
    _set_user_is_active_false(request)
    request.session['sessiondata'] = data

def _set_user_is_active_false(request):
    user = User.objects.get(username = request.user.username)
    data = {
        'user_id' : User.objects.get(username = request.user.username).id,
    }
    request.session['user_id'] = data
    user.is_active = False
    user.save()

def _set_user_is_active_true(request):
    try:
        user_id = get_session_data(request, session_name='user_test_id', name='user_id')
        user = User.objects.get(id = user_id)
        user.is_active = True
        user.save()
        logger.info(
            f'{datetime.datetime.now()} |info| '
            f'Username: {get_username(request)} |'
            f' |login.services._set_user_is_active_true| '
            f'set_user_is_active_true complete for user with id = {user_id}')
    except Exception:
        logger.warning(
            f'{datetime.datetime.now()} |WARNING| '
            f'Username: {get_username(request)} |'
            f' |login.services._set_user_is_active_true| '
            f'Can not set_user_is_active_true')

def verification_email(request):
    save_verify_code(request)
    return redirect('users:vrmail')

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
        logger.info(
            f'{datetime.datetime.now()} |INFO| '
            f'Username: {get_username(request)} |'
            f' |login.services| '
            f'Mail send to {get_user_email(request)} with code {code}')
    except:
        logger.error(
            f'{datetime.datetime.now()} |ERROR| '
            f'Username: {get_username(request)} |'
            f' |login.services| '
            f'Mail send to {get_user_email(request)} with code {code} is failed')
        pass
    return code