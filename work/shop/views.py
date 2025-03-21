from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.views.generic import DetailView
from login.models import User_Status
from .models import *

@ login_required
def basket(request):
    username = request.user.username
    status = User_Status.objects.get(username = request.user.id).Isverified

    basket = Baskets.objects.filter(user=request.user)
    user = request.user
    data={
        'status':status,
        'username':username,
        'basket': basket,
        'user':user
    }
    return render(request, 'shop/Basket.html', data)

def ViewBalance(request):
    balance = User_Status.objects.get(username = request.user.id).balance
    return balance

@ login_required
def shopview(request):
    username = request.user.username
    status = User_Status.objects.get(username=request.user.id).Isverified
    balance = ViewBalance(request)
    products = Products.objects.order_by('mode')

    data = {
        'username':username,
        'status': status,
        'balance': balance,
        'products': products,
    }
    return render(request, 'shop/shopview.html', data)

@ login_required()
def basket_add(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    basket = Baskets.objects.filter(user=request.user, product=product)

    if basket.exists():   #если продукт уже добавлен в корзину пользователя
        basket = basket.first()
        if basket:
            basket.value +=1
            basket.save()
    else:
        Baskets.objects.create(user=request.user, product=product, value = 1)

    return redirect(request.META['HTTP_REFERER'])

def basket_change(request, product_slug):
    ...

def basket_remove(request, product_id):

    cart = Baskets.objects.get(id = product_id)
    cart.delete()

    return redirect(request.META['HTTP_REFERER'])