# Generated by Django 5.1.7 on 2025-04-09 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0061_alter_products_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='type',
            field=models.CharField(choices=[('BL', 'Блок'), ('BO', 'Книга'), ('T', 'Инструмент')], max_length=2, verbose_name='Тип товара'),
        ),
    ]
