from work.global_services import get_username, get_user_verify_is
from django.shortcuts import render, redirect


def about_view(request):
    data = {
        'username': get_username(request),
        'status': get_user_verify_is(request),
    }
    return render(request, 'about/about.html', data)
