from django.db import models

class Rules(models.Model):
    rule_id = models.FloatField('Номер правила')
    crime = models.CharField('Нарушение', max_length=350)
    punishment = models.CharField('Наказание', max_length=200)

    def __str__(self):
        return self.crime

    class Meta:
        verbose_name = 'Правило'
        verbose_name_plural = 'Правила'