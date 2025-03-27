from django.db import models
from django.conf import settings


class Products(models.Model):
    BLOCK = 'BL'
    TOOL = 'T'
    BOOK = 'BO'
    TYPES = {
        (BLOCK, 'Блок'),
        (TOOL, 'Инструмент'),
        (BOOK, 'Книга')
    }

    VANILA = 'V'
    IC2 = 'I'
    TERMO = 'T'
    MODES = {
        (VANILA, 'Ванила'),
        (IC2, 'Indastrial Craft2'),
        (TERMO, 'Termo')
    }

    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    name = models.CharField('Название', max_length=50)
    price = models.PositiveIntegerField('Цена')
    type = models.CharField('Тип товара', max_length=2, choices=TYPES)
    mode = models.CharField('Мод', max_length=1, choices= MODES)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class BasketsQueryset(models.QuerySet):
    """Собственные методы обращения к Baskets"""
    def total_price(self):
        """выводит сумму всех объектов выборки по методу  products_price*
        *- products_price выводит стоимость внутри одной корзины (одного объекта Baskest)"""
        return sum(cart.products_price() for cart in self)

    def total_value(self):
        """Выводит сумму всех объектов выборки по полю value"""
        if self:
            return sum(cart.value for cart in self)
        return 0

class Baskets(models.Model):
    """Структура Корзин. Хранит все объекты корзин всех пользователей"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE,
                                default=None
                                 )
    product = models.ForeignKey(Products,
                                on_delete=models.CASCADE,
                                default=None
                                )
    value = models.IntegerField(default=1)
    is_purchased = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    objects = BasketsQueryset().as_manager()

    def __str__(self):
        return f'{self.user.username} | {self.product.name} | {self.value}'

    def products_price(self):
        return round(self.product.price * self.value , 2)


# Create your models here.
