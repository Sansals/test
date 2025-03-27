from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .services import *
from work.global_services import *
from shop.services import get_user_balance

logger = logging.getLogger(__name__)

def all_profiles_view(request):
    pass

@login_required()
def user_profile_view(request, url_username):
    if get_username(request) == url_username:
        pass
    else:
        return redirect(f'/profiles/{get_username(request)}/')
    data = {
        'status': get_user_verify_is(request),
        'balance': get_user_balance(request)
    }
    return render(request, 'profiles/user_profile.html', data)