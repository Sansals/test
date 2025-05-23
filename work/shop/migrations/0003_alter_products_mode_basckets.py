# Generated by Django 5.1.7 on 2025-03-19 20:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_products_options_rename_prise_products_price_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='mode',
            field=models.CharField(choices=[('I', 'Indastrial Craft2'), ('T', 'Termo'), ('V', 'Ванила')], max_length=1, verbose_name='Мод'),
        ),
        migrations.CreateModel(
            name='Basckets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=1, max_length=6)),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='shop.products')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
            },
        ),
    ]
