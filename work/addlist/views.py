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


#def news_detail_view(request):
    #"""Выводит конкретную запись из Articles по её id"""
    #return NewsDatailView.as_view()



@ login_required()
def create_news_view(request):
    error = ''
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            if get_user_verify_is(request):
                response = form.save(commit=False)
                response.username = get_user(request)
                response.save()
                logger.info(
                    f'{datetime.datetime.now()} |INFO| Username: {get_user(request)} | User create new object in addlist.Articles')
            else:
                save_verify_code(request)
                logger.warning(f'{datetime.datetime.now()} |WARNING| Username: {get_user(request)} | Attempt aborted. User with not verify email attempt add field in addlist.Articles')
                return redirect('vrmail')
        else:
            error = 'Не верно'
    form = ArticlesForm
    data ={
        'username': get_username(request),
        'status': get_user_verify_is(request),
        'form': form,
        'error': error,
    }
    return render(request, 'addlist/createnews.html', data)
