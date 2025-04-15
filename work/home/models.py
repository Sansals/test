from django.db import models

class Rules(models.Model):
    """ Модель правил"""
    rule_id = models.FloatField('Номер правила')
    crime = models.TextField('Нарушение', max_length=350)
    punishment = models.TextField('Наказание', max_length=200, blank=True)

    def __str__(self):
        return self.crime

    class Meta:
        verbose_name = 'Правило'
        verbose_name_plural = 'Правила'