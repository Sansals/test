from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.template.context_processors import request

from .forms import AuthForm, UserRegistrationForm, VrMail
from random import randint
from django.core.mail import send_mail

from .models import Email_Verified


def sendcode(request):
    username = request.user.username
    email = request.user.email
    code = randint(100000, 999999)

    send_mail(
        'Подтверждение учётной записи',
        f'Уважаемый {username}, Ваш код для подтверждения учётной записи по адресу электронной почты: {code}',
        'stereotip.228@gmail.com',
        [email],
        fail_silently=False
    )
    return code

def email_verification(request):
    error = ''

    form = VrMail
    if request.method == "POST":
        form = VrMail(request.POST)
        if form.is_valid():
            data = request.session.pop('sessiondata', {})
            code = data.get('code')
            if int(form.cleaned_data['ver_mail']) == int(code):
                u = Email_Verified.objects.get(username = request.user.id)
                u.Isverified = True
                u.save()
                return redirect ('home')
            else:
                request.session['sessiondata'] = data
                error = f'{request.user.username}, введите коректный код!'
        else:
            error = f'{request.user.username}, введите коректный код!'

    data={
        'form': form,
        'error': error,
        'username': request.user.username,
        'email': request.user.email
    }
    return render(request, 'auth/vermail.html', data)



def auth(request):

    error=''

    user = AuthForm(data=request.POST or None)

    if request.method == "POST":
        if user.is_valid():
            username = user.cleaned_data['username']
            password = user.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user:
                login(request, user)
                status = Email_Verified.objects.get(username=request.user.id).Isverified
                if status == True:
                    return redirect ('home')
                else:
                    data = {
                        'code': sendcode(request)
                    }
                    request.session['sessiondata'] = data

                    return redirect('vrmail')
            else:
                error = 'Пользователя не существует'
        else:
            error = 'Пользователь не существует'



    data = {
        'authform': user,
        'error': error
    }
    return render(request, 'auth/auth.html', data)


def registration(request):
    if not request.user.is_authenticated:
        error=''
        form = UserRegistrationForm(data= request.POST or None)
        if request.method == "POST":
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password'])
                user.save()
                login(request, authenticate(username=user.username, password=form.cleaned_data['password']))
                u = User.objects.get(username=request.user.username)
                Email_Verified.objects.create(username=u)
                data={
                    'code': sendcode(request)
                }
                request.session['sessiondata'] = data

                return redirect('vrmail')

    else:
        return redirect('home')

    data = {
        'form':form,
        'error': error
    }
    return render(request, 'auth/reg.html', data)

def logout_view(request):
    logout(request)
    return redirect('home')
# Create your views here.