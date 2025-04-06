from django.db import models
from django.conf import settings
from login.models import User_Status


class Public_Chat(models.Model):
    username = models.ForeignKey(User_Status,
                                 on_delete=models.SET_DEFAULT,
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


class Articles(models.Model):
    """Модель новостей"""
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField(auto_now_add=True)
    username = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_DEFAULT,
                             default=None, null=True, blank=True
                             )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class ForumQuestions(models.Model):
    PROBLEMS_WITH_GAME_CLIENT = 'Проблемы с клиентом игры'
    PROBLEMS_WITH_SITE = 'Проблемы с сайтом'
    PROBLEMS_WITH_PAYMENT = 'Проблемы с оплатой'
    GET_ANSWER_THE_QUESTION = 'Получить ответ на вопрос'
    COMPLAINT_ABOUT_THE_USER = 'Сообщить о нарушении правил игроком'
    APPEAL_THE_PUNISHMENT = 'Обжаловать наказание'
    COMPLAINT_ABOUT_THE_ADMIN = 'Сообщить о нарушении правил со стороны Администрации'
    COMPLAINT_ABOUT_THE_CLAN = 'Сообщить о нарушении правил кланом/группой игроков'

    SUBJECT = {
        (PROBLEMS_WITH_GAME_CLIENT, 'Проблемы с клиентом игры'),
        (PROBLEMS_WITH_SITE, 'Проблемы с сайтом'),
        (PROBLEMS_WITH_PAYMENT, 'Проблемы с оплатой'),
        (GET_ANSWER_THE_QUESTION, 'Получить ответ на вопрос'),
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
                                related_name = 'defendant',
                                verbose_name = 'Ответчик'
                                 )
    question = models.TextField('Заявление', max_length= 600 )
    proofs = models.CharField('Доказательства', max_length= 600)
    date = models.DateTimeField(auto_now_add=True)
    is_anonymous = models.BooleanField(default=False)
    is_resolved = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Вопрос на форумe'
        verbose_name_plural = 'Вопросы с форума'

    def __str__(self):
        return f'{self.subject} | {self.user.username} | {self.defendant.username} | {self.question}'


class ForumAnswer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             default=None,
                             related_name='user',
                             verbose_name='Отвечающий'
                             )
    question = models.ForeignKey(ForumQuestions,
                                verbose_name = 'Обращение',
                               on_delete=models.CASCADE,
                                 )
    answer = models.TextField('Ответ', max_length= 600 )
    is_anonymous = models.BooleanField(default=False)

# Create your models here.
