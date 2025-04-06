from .models import Articles, Public_Chat
from login.models import User_Status
from django.shortcuts import redirect, render
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
import logging
import datetime
from login.models import User_Status
from .forms import PublicMessageForm
from django.contrib.auth.models import User

from work.global_services import get_user

def get_stuff_users():
    return User_Status.objects.filter(is_staff=True)

def get_public_messages():
    return Public_Chat.objects.order_by('-date')


def save_message(request):
    form= PublicMessageForm()
    if request.user.is_authenticated:
        form = PublicMessageForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.username = User_Status.objects.get(username=request.user.id)
            response.save()
            form = PublicMessageForm()
    return form

def get_rich_users():
    return User_Status.objects.order_by('-balance')[:3]


logger = logging.getLogger(__name__)

class ArticlesDatailView(DetailView):
    try:
        model = Articles
        template_name = 'forum/details_view.html'
        context_object_name = 'article'
    except ValueError:
        logger.warning(f'{datetime.datetime.now()} Не удалось получить объекты/объекты отсутствуют в addlist.Articles')
    except Exception:
        logger.error(f'{datetime.datetime.now()} Неизвестная ошибка при работе с addlist.Articles. Файл addlist.services')