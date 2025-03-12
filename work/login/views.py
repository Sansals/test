from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import AuthForm

def auth(request):

    info=''

    user = AuthForm(data=request.POST or None)
    if request.method == "POST":
        if user.is_valid():
            username = user.cleaned_data['username']
            password = user.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user:
                login(request, user)
                return redirect ('home')
                info = 'Успешно!'
            else:
                info = 'Пользователя не существует'
        else:
            info = 'Форма невалидна'



    data = {
        'AuthForm': user,
        'info': info
    }
    return render(request, 'auth/auth.html', data)
# Create your views here.
