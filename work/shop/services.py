from .models import Baskets, Products
from login.models import User_Status
from work.global_services import get_user, get_username
import logging
import datetime

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


def get_all_user_baskets(request):
    """Берёт все объекты из Baskets для текушего пользователя"""
    try:
        products = Baskets.objects.filter(user=get_user(request))
        logger.info(
            f'{datetime.datetime.now()} |INFO| '
            f'Username: {get_username(request)} |'
            f' |shop.services| '
            f'User get all objects from Baskets')
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
        products = Products.objects.order_by('mode')
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
    basket = Baskets.objects.filter(user=get_user(request), product=_get_product_by_slug(request, product_slug))
    return basket

def _create_new_basket(request, product_slug):
    Baskets.objects.create(user=get_user(request), product=_get_product_by_slug(request, product_slug), value=1)