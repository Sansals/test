from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .services import *
from work.global_services import *
from shop.services import get_user_balance, basket_value

logger = logging.getLogger(__name__)

def all_profiles_view(request):
    pass

@login_required()
def user_profile_view(request, url_username):
    if get_username(request) == url_username:
        data = {
            'user_status_object': get_object_from_user_status(request),
            'user_object':get_user(request),
            'basket_value': basket_value(request),
        }
    else:
        data = {
            'user_status_object': get_user_status_profile_object(url_username),
            'user_object':get_user_profile_object(url_username),
            'basket_value': basket_value(request),
        }

    return render(request, 'profiles/user_profile.html', data)
