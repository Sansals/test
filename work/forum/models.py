from django.db import models
from django.conf import settings
from login.models import User_Status
from datetime import date

class Public_Chat(models.Model):
    """Модель для хранения объектов сообщений общего чата"""
    username = models.ForeignKey(User_Status,
                                 on_delete=models.CASCADE,
                                 default=None, null=True, blank=True
                                 )
    text = models.CharField('Сообщение', max_length=300)
    date = models.DateTimeField(auto_now_add=True)

    def user_avatar(self):
        return self.username.avatar

    class Meta:
        verbose_name = 'Сообщение в общий чат'
        verbose_name_plural = 'Сообщения в общем чате'

    def __str__(self):
        return f'{self.username.username} | {self.text} | {self.date}'


class ForumTechQuestions(models.Model):
    """Модель для хранения объектов технических вопросов"""
    PROBLEMS_WITH_GAME_CLIENT = 'Проблемы с клиентом игры'
    PROBLEMS_WITH_SITE = 'Проблемы с сайтом'
    PROBLEMS_WITH_PAYMENT = 'Проблемы с оплатой'
    GET_ANSWER_THE_QUESTION = 'Получить ответ на вопрос'

    SUBJECT = {
        (PROBLEMS_WITH_GAME_CLIENT, 'Проблемы с клиентом игры'),
        (PROBLEMS_WITH_SITE, 'Проблемы с сайтом'),
        (PROBLEMS_WITH_PAYMENT, 'Проблемы с оплатой'),
        (GET_ANSWER_THE_QUESTION, 'Получить ответ на вопрос'),
    }
    subject = models.CharField('Раздел форума', max_length=52, choices= SUBJECT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE,
                                default=None,
                                related_name='questioner',
                                verbose_name = 'Создатель тикета'
                                 )
    question = models.TextField('Вопрос', max_length= 600 )
    proofs = models.CharField('Скриншот проблемы', max_length= 600, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Вопрос на форумe'
        verbose_name_plural = 'Вопросы с форума'

    def __str__(self):
        return f'{self.subject} | {self.user.username} | {self.question}'


class ForumComplaints(models.Model):
    """Модель для хранения объектов жалоб на форуме"""
    COMPLAINT_ABOUT_THE_USER = 'Сообщить о нарушении правил игроком'
    APPEAL_THE_PUNISHMENT = 'Обжаловать наказание'
    COMPLAINT_ABOUT_THE_ADMIN = 'Сообщить о нарушении правил со стороны Администрации'
    COMPLAINT_ABOUT_THE_CLAN = 'Сообщить о нарушении правил кланом/группой игроков'

    SUBJECT = {
        (COMPLAINT_ABOUT_THE_USER, 'Сообщить о нарушении правил игроком'),
        (APPEAL_THE_PUNISHMENT, 'Обжаловать наказание'),
        (COMPLAINT_ABOUT_THE_ADMIN, 'Сообщить о нарушении правил со стороны Администрации'),
        (COMPLAINT_ABOUT_THE_CLAN, 'Сообщить о нарушении правил кланом/группой игроков'),
    }

    subject = models.CharField('Раздел форума', max_length=52, choices= SUBJECT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE,
                                default=None,
                                related_name='claimant',
                                verbose_name = 'Заявитель'
                                 )
    defendant = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE,
                                  default=None,
                                  related_name='defendant',
                                  verbose_name='Нарушитель'
                                  )
    question = models.TextField('Заявление', max_length= 600 )
    proofs = models.CharField('Доказательства', max_length= 600)
    date = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)
    is_anonymous = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Жалобу на форумe'
        verbose_name_plural = 'Жалобы с форума'

    def __str__(self):
        return f'{self.subject} | {self.user.username} | {self.defendant.username} | {self.question}'


class ForumTechAnswer(models.Model):
    """Модель для хранения объектов ответов на технические вопросы"""
    user = models.ForeignKey(User_Status,
                             on_delete=models.CASCADE,
                             default=None,
                             related_name='responsible_tech_user',
                             verbose_name='Отвечающий'
                             )
    question = models.ForeignKey(ForumTechQuestions,
                                verbose_name = 'Вопрос',
                               on_delete=models.CASCADE,
                                 )
    date = models.DateTimeField(auto_now_add=True)
    answer = models.CharField('Ответ', max_length= 600 )
    is_anonymous = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Ответ на технический вопрос'
        verbose_name_plural = 'Ответы на технические вопросы'

    def __str__(self):
        return f'{self.user.username} | {self.question.user.username} | {self.answer}'

class ForumComplaintAnswer(models.Model):
    """Модель для хранения объектов ответов на жалобы"""
    user = models.ForeignKey(User_Status,
                             on_delete=models.CASCADE,
                             default=None,
                             related_name='responsible_complaint_user',
                             verbose_name='Отвечающий'
                             )
    question = models.ForeignKey(ForumComplaints,
                                verbose_name = 'Жалоба',
                               on_delete=models.CASCADE,
                                 )
    date = models.DateTimeField(auto_now_add=True, blank=True)
    answer = models.TextField('Ответ', max_length= 600 )
    is_anonymous = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Ответ на жалобу'
        verbose_name_plural = 'Ответы на жалобы'

# Create your models here.
