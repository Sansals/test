from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template.context_processors import request
from django.views.generic import DetailView
from login.models import User_Status
from .models import *

@ login_required
def basket(request):
    username = request.user.username
    status = User_Status.objects.get(username = request.user.id).Isverified

    products = Baskets.objects.order_by('user')
    user = request.user
    data={
        'status':status,
        'username':username,
        'products': products,
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
    products = Products.objects.order_by('name')

    data = {
        'username':username,
        'status': status,
        'balance': balance,
        'products': products,
    }
    return render(request, 'shop/shopview.html', data)