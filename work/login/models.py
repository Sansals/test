from django.conf import settings
from django.db import models
from django.urls import reverse

def user_avatar_directory(instance: '', filename: str) -> str:
    return 'users/user_{pk}/avatars/{filename}'.format(
        pk=instance.pk,
        filename = filename,
    )

class User_Status(models.Model):
    user_id = models.AutoField (primary_key=True)
    username = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Пользователь')
    avatar = models.ImageField('Аватар', upload_to=user_avatar_directory, default='login/avatars/stive.jpg')
    balance = models.IntegerField('Баланс', default=0)
    Isverified = models.BooleanField('Верификация почты', default=False)
    is_staff = models.BooleanField('Статус Администратора', default=False)
    is_moderator = models.BooleanField('Статус Модератора', default=False)

    def get_absolute_url(self):
        return reverse("profile", kwargs={'url_username': self.username})

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = 'статусы пользователей'
        verbose_name_plural = 'Статусы пользователей'
        # Create your models here.

