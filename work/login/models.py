from django.conf import settings
from django.db import models

class Email_Verified(models.Model):
    user_id = models.AutoField (primary_key=True)
    username = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    Isverified = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.username}'
        # Create your models here.

