from django.shortcuts import render
from django.template.context_processors import request


def home(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'нет пользователя'

    data = {
        'username': username,
    }

    return render(request,'home/index.html', data)

# Create your views here.
