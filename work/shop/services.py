from .models import Baskets, Products
from login.models import User_Status
from work.global_services import get_user, get_username
import logging
import datetime
from django.shortcuts import redirect

logger = logging.getLogger(__name__)

def add_product_by_slug_in_basket_by_user(request, product_slug):
    basket = _filter_baskets_by_user_and_product(request,product_slug)
    if basket.exists():   #если продукт уже добавлен в корзину пользователя
        basket = basket.first()
        if basket:
            basket.value +=1
            basket.save()
    else:
        _create_new_basket(request, product_slug)

def get_purchased_baskets(request):
    products = Baskets.objects.filter(user=get_user(request), is_purchased=True)
    return products


def get_all_user_baskets(request):
    """Берёт все объекты из Baskets для текушего пользователя"""
    """Только не оплаченные корзины"""
    try:
        products = Baskets.objects.filter(user=get_user(request), is_purchased = False)
        logger.info(
            f'{datetime.datetime.now()} |INFO| '
            f'Username: {get_username(request)} |'
            f' |shop.services| '
            f'User get all objects from Baskets'
        )
        return products
    except Exception:
        logger.error(
            f'{datetime.datetime.now()} |ERROR| '
            f'Username: {get_username(request)} |'
            f' |shop.services| '
            f'User failed get all objects from Baskets')

def get_user_balance(request):
    try:
        balance = User_Status.objects.get(username = request.user.id).balance
        logger.info(
            f'{datetime.datetime.now()} |INFO| '
            f'Username: {get_username(request)} |'
            f' |shop.services| '
            f'User get his balance')
        return balance
    except Exception:
        logger.error(
            f'{datetime.datetime.now()} |ERROR| '
            f'Username: {get_username(request)} |'
            f' |shop.services| '
            f'Get user balance is failed!')
        pass

def get_all_products(request):
    try:
        products = Products.objects.order_by('-mode')
        logger.info(
            f'{datetime.datetime.now()} |INFO| '
            f'Username: {get_username(request)} |'
            f' |shop.services| '
            f'User get all product!')
        return products
    except Exception:
        logger.error(
            f'{datetime.datetime.now()} |ERROR| '
            f'Username: {get_username(request)} |'
            f' |shop.services| '
            f'User is failed get all product!')
        pass

def calculation_total_price(request):
    return get_all_user_baskets(request).total_price()

def comparison_total_price_with_balance_is(request):
    if get_user_balance(request) >= calculation_total_price(request):
        logger.info(
            f'{datetime.datetime.now()} |INFO| '
            f'Username: {get_username(request)} |'
            f' |shop.services| '
            f'comparison_total_price_with_balance True!')
        return True
    else:
        logger.warning(
            f'{datetime.datetime.now()} |Warning| '
            f'Username: {get_username(request)} |'
            f' |shop.services| '
            f'comparison_total_price_with_balance False')
        return False

def update_user_balance(request):
    user = User_Status.objects.get(username = get_user(request))
    user.balance = get_user_balance(request) - calculation_total_price(request)
    user.save()

def update_baskets_model(request):
    products = Baskets.objects.filter(user=get_user(request), is_purchased = False)
    products.update(is_purchased=True)

def _get_product_by_slug(request, product_slug):
    try:
        product = Products.objects.get(slug=product_slug)
        logger.info(
            f'{datetime.datetime.now()} |INFO| '
            f'Username: {get_username(request)} |'
            f' |shop.services| '
            f'Product get by Product.slug')
        return product
    except ValueError:
        logger.error(
            f'{datetime.datetime.now()} |ERROR| '
            f'Username: {get_username(request)} |'
            f' |shop.services| '
            f'Product with this slug is not exists!')
        pass

def _filter_baskets_by_user_and_product(request, product_slug):
    """Выводит все неоплаченные объекты из Baskets, содержащие товар и относящиеся к пользователю"""
    basket = Baskets.objects.filter(user=get_user(request), product=_get_product_by_slug(request, product_slug), is_purchased = False)
    return basket

def _create_new_basket(request, product_slug):
    Baskets.objects.create(user=get_user(request), product=_get_product_by_slug(request, product_slug), value=1)

def basket_value(request):
    baskets = get_all_user_baskets(request)
    return baskets.total_value