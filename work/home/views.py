from django.shortcuts import render

from .services import *
from shop.services import basket_value
from work.global_services import *


def rules_view(request):
    data = {
        'username': get_username(request),
        'status': get_user_verify_is(request),
        'rules': get_rules_all(request),
        'basket_value': basket_value(request),
    }
    return render(request, 'home/rules.html', data)

def home_view(request):
    data = {
        'user_id': get_user_id(request),
        'username': get_username(request),
        'status': get_user_verify_is(request),
        'news': get_all_articles(request),
        'basket_value': basket_value(request),
    }
    return render(request,'home/index.html', data)

# Create your views here.
