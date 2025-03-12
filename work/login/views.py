from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import AuthForm, UserRegistrationForm

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
        'authform': user,
        'info': info
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
                return redirect('home')
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