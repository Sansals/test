from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ArticlesForm, ForumTechSupportForm
from work.global_services import get_user

from .models import Public_Chat

from shop.services import basket_value
from .services import *
from work.global_services import get_username, get_user_verify_is
from login.services import save_verify_code
import logging
import datetime

logger = logging.getLogger(__name__)

@login_required()
def techsupport_form_view(request):
    form = ForumTechSupportForm(request.POST)
    if form.is_valid():
        response = form.save(commit=False)
        response.user = request.user
        response.save()
        form = ForumTechSupportForm()
    return render(request, 'forum/techsupport/form.html', {'form':form })

@login_required()
def forum_view(request):
    data ={
        'username': get_username(request),
        'status': get_user_verify_is(request),
        'rich_users_top': get_rich_users(),
        'message_input': save_message(request),
        'all_messages': get_public_messages,
        'stuff_users': get_stuff_users,
        'basket_value': basket_value(request)
    }
    return render(request, 'forum/forum_index.html', data)
