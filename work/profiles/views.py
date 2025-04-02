from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .services import *
from work.global_services import *
from shop.services import get_user_balance
from .forms import AvatarUpdateForm

from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin
from login.models import User_Status

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
        'balance': get_user_balance(request),
        'user_object': get_object_from_user_status(request),
    }
    return render(request, 'profiles/user_profile.html', data)

class AvatarUpdateView(UserPassesTestMixin, UpdateView):

    def test_func(self):
        if (self.request.user.id == self.get_object().username.id
            or self.request.user.is_staff):
            return True

    model = User_Status
    template_name = 'profiles/avatar_update.html'
    form_class = AvatarUpdateForm