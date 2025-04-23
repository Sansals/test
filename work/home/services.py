from .models import Rules, News, News_Comments
from login.models import User_Status
from django.contrib.auth.models import User
from .forms import CommentsForm
import logging
import datetime
from django.shortcuts import redirect

from work.global_services import get_username

logger = logging.getLogger(__name__)

def get_len_of_users():
    return len(User.objects.all())

def get_users_avatars():
    return User_Status.objects.all().order_by('user_id')[:5]

def get_news_len():
    return len(get_all_news())

def get_all_news():
    return News.objects.all().order_by('-date')

def get_new_for_id(id):
    new = News.objects.get(pk=id)
    return new

def get_new_comments_for_id(id):
    new = News.objects.get(pk=id)
    comments = News_Comments.objects.filter(new = new).order_by('-date')
    return comments

def comment_save(request, id):
    form = CommentsForm(request.POST)
    if form.is_valid():
        response = form.save(commit=False)
        response.user = User_Status.objects.get(username=request.user.id)
        response.new = get_new_for_id(id)
        response.save()
        form = CommentsForm()
    return form

def get_rules_all(request):
    """Берёт все объекты таблицы Rules, сортирует их по ID записи"""
    try:
        all_rules = Rules.objects.order_by('rule_id')
        logger.info(f'{datetime.datetime.now()} |INFO| Username: {get_username(request)} | User get all objects from home.Rules')
    except ValueError:
        logger.info(
            f'{datetime.datetime.now()} |INFO| '
            f'Username: {get_username(request)} |'
            f' |home.services|'
            f'ValueError in get all objects from home.Rules')
    except Exception:
        logger.info(
            f'{datetime.datetime.now()} |INFO| '
            f'Username: {get_username(request)} |'
            f' |home.services|'
            f'Exception in get all objects from home.Rules')
    return all_rules