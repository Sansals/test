from django.contrib.auth.models import User
from django.views.generic import DetailView
import logging
import datetime
from login.models import User_Status
from work.global_services import *

def get_object_from_user_status(request):
    user_object = User_Status.objects.get(username = get_user(request))
    return user_object