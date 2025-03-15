from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Email_Verified(models.Model):
    user = models.CharField(max_length=50)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user
