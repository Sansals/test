from django.contrib.auth.models import User
from django.views.generic import DetailView
import logging
import datetime
from .forms import AvatarUpdateForm
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin
from login.models import User_Status
from work.global_services import *
from login.services import save_verify_code

def verification_email():
    save_verify_code(request)
    redirect('vrmail')

def get_user_profile_object(username):
    return User.objects.get(username=username)

def get_user_status_profile_object(username):
    user = User.objects.get(username=username)
    return User_Status.objects.get(username=user)

def get_object_from_user_status(request):
    user_object = User_Status.objects.get(username = get_user(request))
    return user_object

class AvatarUpdateView(UserPassesTestMixin, UpdateView):

    def test_func(self):
        if (self.request.user.id == self.get_object().username.id
            or self.request.user.is_staff):
            return True

    model = User_Status
    template_name = 'profiles/avatar_update.html'
    form_class = AvatarUpdateForm