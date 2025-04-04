from django.db import models
from django.conf import settings


class Public_Chat(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.SET_DEFAULT,
                                 default=None, null=True, blank=True
                                 )
    text = models.CharField('Сообщение', max_length=300)
    date = models.DateTimeField(auto_now_add=True)

    def user_avatar(self):
        return self.username.avatar

    class Meta:
        verbose_name = 'Сообщение в общий чат'
        verbose_name_plural = 'Сообщения в общем чате'

    def __str__(self):
        return f'{self.username.username} | {self.text} | {self.date}'


class Articles(models.Model):
    """Модель новостей"""
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField(auto_now_add=True)
    username = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_DEFAULT,
                             default=None, null=True, blank=True
                             )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

# Create your models here.
