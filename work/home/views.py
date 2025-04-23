from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .services import *
from shop.services import basket_value
from work.global_services import *
from forum.services import get_user_status_object


def news_view(request):
    """Метод представления страницы с новостями"""
    data={
        'basket_value': basket_value(request),
        'all_news': get_all_news(),
    }
    return render(request, 'news/news.html', data)

def new_article_view(request, id):
    """Метод представления страницы конкретной новости"""
    if request.user.is_authenticated:
        try:
            data ={
                'basket_value': basket_value(request),
                'new': get_new_for_id(id),
                'new_comments': get_new_comments_for_id(id),
                'comment_input' : comment_save(request, id),
                'user_status_object': get_user_status_object(request),
            }
        except Exception:
            return redirect('new_not_founded')
    else:
        try:
            data ={
                'new': get_new_for_id(id),
                'new_comments': get_new_comments_for_id(id),
            }
        except Exception:
            return redirect('new_not_founded')
    return render(request, 'news/new_detail.html', data)

def new_article_not_founded(request):
    """Метод представления страницы не существующей новости (по PK)"""
    data = {
        'basket_value': basket_value(request),
    }
    return render(request, 'news/new_not_founded.html', data)

def rules_view(request):
    """Метод представления страницы правил"""
    data = {
        'rules': get_rules_all(request),
        'basket_value': basket_value(request),
    }
    return render(request, 'home/rules.html', data)

@login_required()
def installers_view(request):
    """Метод представления страницы с тех. требованиями и версиями клиента"""
    return render(request, 'home/installers.html')

def home_view(request):
    """Метод представления главной страницы"""
    data = {
        'basket_value': basket_value(request),
        'news': get_all_news()[:3],
        'news_len': get_news_len(),
        'users_avatars': get_users_avatars(),
        'users_len': get_len_of_users(),
    }
    return render(request,'home/index.html', data)

# Create your views here.
