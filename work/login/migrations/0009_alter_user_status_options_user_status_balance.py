# Generated by Django 5.1.7 on 2025-03-16 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_rename_email_verified_user_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user_status',
            options={'verbose_name': 'статусы пользователю', 'verbose_name_plural': 'Статусы пользователей'},
        ),
        migrations.AddField(
            model_name='user_status',
            name='balance',
            field=models.IntegerField(default=0),
        ),
    ]
