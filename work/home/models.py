from django.db import models
from login.models import User_Status

def news_img_directory(instance: '', filename: str) -> str:
    """Кастомный метод сохранения пути до изображения в БД"""
    return 'news/{pk}{filename}'.format(
        pk=instance.pk,
        filename = filename,
    )

class News(models.Model):
    """Модель для хранения объектов новостей"""
    title = models.CharField(max_length=300)
    img = models.ImageField(upload_to=news_img_directory, default='news/news_img.jpg')
    user = models.ForeignKey(User_Status,
                                 on_delete=models.SET_DEFAULT,
                                 default=None, null=True, blank=True
                                 )
    date = models.DateTimeField(auto_now_add=True)
    article = models.TextField(max_length=2000)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class News_Comments(models.Model):
    """Модель под комментарии к новостям"""
    new = models.ForeignKey(News,
                             on_delete=models.CASCADE,
                             default=None, null=True, blank=True
                             )
    user = models.ForeignKey(User_Status,
                             on_delete=models.SET_DEFAULT,
                             default='Пользователь удалён', null=True, blank=True
                             )
    date = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=350)

    def __str__(self):
        return f'{self.user} | {self.comment} | {self.date}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии под новостями'


class Rules(models.Model):
    """ Модель правил"""
    rule_id = models.FloatField('Номер правила')
    crime = models.TextField('Нарушение', max_length=550)
    punishment = models.TextField('Наказание', max_length=200, blank=True)

    def __str__(self):
        return self.crime

    class Meta:
        verbose_name = 'Правило'
        verbose_name_plural = 'Правила'