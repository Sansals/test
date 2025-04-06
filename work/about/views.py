from work.global_services import get_username, get_user_verify_is
from django.shortcuts import render, redirect

from shop.services import basket_value


def about_view(request):
    data = {
        'username': get_username(request),
        'status': get_user_verify_is(request),
        'basket_value': basket_value(request),
    }
    return render(request, 'about/about.html', data)
