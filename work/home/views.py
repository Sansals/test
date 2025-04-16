from django.shortcuts import render

from .services import *
from shop.services import basket_value
from work.global_services import *
from forum.services import get_user_status_object


def news_view(request):
    data={
        'basket_value': basket_value(request),
        'all_news': get_all_news(),
    }
    return render(request, 'news/news.html', data)

def new_article_view(request, id):
    try:
        data ={
            'basket_value': basket_value(request),
            'new': get_new_for_id(id),
            'new_comments': get_new_comments_for_id(id),
            'comment_input' : comment_save(request),
            'user_status_object': get_user_status_object(request),
        }
    except Exception:
        return redirect('new_not_founded')
    return render(request, 'news/new_detail.html', data)

def new_article_not_founded(request):
    data = {
        'basket_value': basket_value(request),
    }
    return render(request, 'news/new_not_founded.html', data)

def rules_view(request):
    data = {
        'rules': get_rules_all(request),
        'basket_value': basket_value(request),
    }
    return render(request, 'home/rules.html', data)

def home_view(request):
    data = {
        'user_id': get_user_id(request),
        'username': get_username(request),
        'status': get_user_verify_is(request),
        'basket_value': basket_value(request),
        'news': get_all_news()[:3],
        'news_len': get_news_len,
    }
    return render(request,'home/index.html', data)

# Create your views here.
