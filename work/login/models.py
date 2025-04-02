from django.conf import settings
from django.db import models

class User_Status(models.Model):
    user_id = models.AutoField (primary_key=True)
    username = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='login/avatars/', default='login/avatars/stive.jpg')
    balance = models.IntegerField(default=0)
    Isverified = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = 'статусы пользователей'
        verbose_name_plural = 'Статусы пользователей'
        # Create your models here.

