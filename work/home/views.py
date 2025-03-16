from django.shortcuts import render
from django.template.context_processors import request
from login.models import Email_Verified


def home(request):
    if request.user.is_authenticated:
        username = request.user.username
        status = Email_Verified.objects.get(username = request.user.id).Isverified
    else:
        username = 'нет пользователя'
        status = ''


    data = {
        'username': username,
        'status': status
    }

    return render(request,'home/index.html', data)

# Create your views here.
