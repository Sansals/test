# Generated by Django 5.1.7 on 2025-03-26 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_articles_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='username',
            new_name='user',
        ),
    ]
