from django.shortcuts import render
from django.template.context_processors import request
from login.models import User_Status
from .models import Rules

from addlist.models import Articles


def rules(request):
    if request.user.is_authenticated:
        username = request.user.username
        status = User_Status.objects.get(username=request.user.id).Isverified
    else:
        username = 'нет пользователя'
        status = ''

    rules = Rules.objects.order_by('rule_id')
    data = {
        'username': username,
        'status': status,
        'rules': rules
    }

    return render(request, 'home/rules.html', data)

def home(request):
    if request.user.is_authenticated:
        username = request.user.username
        status = User_Status.objects.get(username = request.user.id).Isverified
    else:
        username = 'нет пользователя'
        status = ''
    news = Articles.objects.order_by('-date')
    data = {
        'username': username,
        'status': status,
        'news': news
    }

    return render(request,'home/index.html', data)

# Create your views here.
