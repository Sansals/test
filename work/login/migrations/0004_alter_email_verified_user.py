# Generated by Django 5.1.7 on 2025-03-15 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email_verified',
            name='user',
            field=models.TextField(),
        ),
    ]
