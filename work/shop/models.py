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

    name = models.CharField('Название', max_length=50)
    price = models.IntegerField('Цена', max_length=7)
    type = models.CharField('Тип товара', max_length=2, choices=TYPES)
    mode = models.CharField('Мод', max_length=1, choices= MODES)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Baskets(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE,
                                default=None
                                 )
    product = models.ForeignKey(Products,
                                on_delete=models.CASCADE,
                                default=None
                                )
    value = models.IntegerField(max_length=6,
                                default=1)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
# Create your models here.
