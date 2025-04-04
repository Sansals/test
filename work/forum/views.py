from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ArticlesForm
from work.global_services import get_user

from .services import *
from work.global_services import get_username, get_user_verify_is
from login.services import save_verify_code
import logging
import datetime

logger = logging.getLogger(__name__)

@login_required()
def forum_view(request):
    data ={
        'username': get_username(request),
        'status': get_user_verify_is(request),
        'rich_users_top': get_rich_users(),
        'message_input': save_message(request),
        'all_messages': get_public_messages,
        'stuff_users': get_stuff_users,
    }
    return render(request, 'forum/forum_index.html', data)
