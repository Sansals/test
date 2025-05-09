# Generated by Django 5.1.7 on 2025-03-19 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.RenameField(
            model_name='products',
            old_name='prise',
            new_name='price',
        ),
        migrations.AlterField(
            model_name='products',
            name='mode',
            field=models.CharField(choices=[('I', 'Indastrial Craft2'), ('V', 'Ванила'), ('T', 'Termo')], max_length=1, verbose_name='Мод'),
        ),
        migrations.AlterField(
            model_name='products',
            name='type',
            field=models.CharField(choices=[('BO', 'Книга'), ('BL', 'Блок'), ('T', 'Инструмент')], max_length=2, verbose_name='Тип товара'),
        ),
    ]
