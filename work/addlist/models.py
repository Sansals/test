from django.db import models
from django.conf import settings


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
