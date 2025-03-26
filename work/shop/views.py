from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.views.generic import DetailView
from login.models import User_Status
from .models import *

from work.global_services import get_username, get_user_verify_is, get_user
from .services import get_all_user_baskets, get_user_balance, get_all_products, add_product_by_slug_in_basket_by_user

@ login_required
def basket_view(request):
    data={
        'status':get_user_verify_is(request),
        'username':get_username(request),
        'basket': get_all_user_baskets(request),
        'user':get_user(request),
        'balance': get_user_balance(request)
    }
    return render(request, 'shop/Basket.html', data)

def shop_view(request):
    data = {
        'username':get_username(request),
        'status':get_user_verify_is(request),
        'products': get_all_products(request),
    }
    return render(request, 'shop/shopview.html', data)

@ login_required()
def basket_add(request, product_slug):
    add_product_by_slug_in_basket_by_user(request, product_slug)
    return redirect(request.META['HTTP_REFERER'])

def basket_change(request, product_slug):
    ...

def basket_remove(request, product_id):

    cart = Baskets.objects.get(id = product_id)
    cart.delete()

    return redirect(request.META['HTTP_REFERER'])