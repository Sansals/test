from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .services import *
from work.global_services import *
from shop.services import get_user_balance, basket_value

logger = logging.getLogger(__name__)

def all_profiles_view(request):
    pass

@login_required()
def user_profile_answers_view(request, url_username):
    if get_username(request) == url_username:
        data = {
            'user_status_object': get_object_from_user_status(request),
            'user_object':get_user(request),
            'basket_value': basket_value(request),
            'value_user_articles': get_value_user_articles(url_username),
            'value_user_answer': get_value_user_answer(url_username),
            'value_user_comments': get_value_user_comments(url_username),


            'all_user_answers': get_all_user_answers(url_username),
        }
    else:
        try:
            User.objects.get(username=url_username)
            data = {
                'user_status_object': get_user_status_profile_object(url_username),
                'user_object': get_user_profile_object(url_username),
                'basket_value': basket_value(request),
                'value_user_articles': get_value_user_articles(url_username),
                'value_user_answer': get_value_user_answer(url_username),
                'value_user_comments': get_value_user_comments(url_username),
            }
        except User.DoesNotExist:
            return redirect(f'/profiles/{get_username(request)}/')
    return render(request, 'profiles/user_profile_answers.html', data)

@login_required()
def user_profile_comments_view(request, url_username):
    if get_username(request) == url_username:
        data = {
            'user_status_object': get_object_from_user_status(request),
            'user_object':get_user(request),
            'basket_value': basket_value(request),
            'value_user_articles': get_value_user_articles(url_username),
            'value_user_answer': get_value_user_answer(url_username),
            'value_user_comments': get_value_user_comments(url_username),


            'all_user_comments': get_all_user_comments(url_username),
        }
    else:
        try:
            User.objects.get(username=url_username)
            data = {
                'user_status_object': get_user_status_profile_object(url_username),
                'user_object': get_user_profile_object(url_username),
                'basket_value': basket_value(request),
                'value_user_articles': get_value_user_articles(url_username),
                'value_user_answer': get_value_user_answer(url_username),
                'value_user_comments': get_value_user_comments(url_username),
            }
        except User.DoesNotExist:
            return redirect(f'/profiles/{get_username(request)}/')
    return render(request, 'profiles/user_profile_comments.html', data)

@login_required()
def user_profile_view(request, url_username):
    if get_username(request) == url_username:
        data = {
            'user_status_object': get_object_from_user_status(request),
            'user_object':get_user(request),
            'basket_value': basket_value(request),
            'value_user_articles': get_value_user_articles(url_username),
            'value_user_answer': get_value_user_answer(url_username),
            'value_user_comments': get_value_user_comments(url_username),

            'all_open_user_articles': get_all_open_user_articles(url_username),
            'all_closed_user_articles': get_all_closed_user_articles(url_username),
        }
    else:
        try:
            User.objects.get(username=url_username)
            data = {
                'user_status_object': get_user_status_profile_object(url_username),
                'user_object': get_user_profile_object(url_username),
                'basket_value': basket_value(request),
                'value_user_articles': get_value_user_articles(url_username),
                'value_user_answer': get_value_user_answer(url_username),
                'value_user_comments': get_value_user_comments(url_username),
            }
        except User.DoesNotExist:
            return redirect(f'/profiles/{get_username(request)}/')

    return render(request, 'profiles/user_profile.html', data)
