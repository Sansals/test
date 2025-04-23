from .models import Public_Chat, ForumTechQuestions, ForumTechAnswer, ForumComplaints, ForumComplaintAnswer
from login.models import User_Status
from django.shortcuts import redirect, render
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
import logging
import datetime
from login.models import User_Status
from .forms import PublicMessageForm
from django.contrib.auth.models import User

from work.global_services import get_user

def get_complaints_len():
    """Метод вывода кол-ва всех жалоб на форуме"""
    return len(ForumComplaints.objects.all())

def get_questions_len():
    """Метод вывода кол-ва всех писем в тех поддержку на форуме"""
    return len(ForumTechQuestions.objects.all())

def get_answers(pk):
    """Метод вывода объектов всех ответов по конкретному вопросу на форуме"""
    question = ForumTechQuestions.objects.get(pk=pk)
    return ForumTechAnswer.objects.filter(question=question).order_by('-date')

def get_answers_for_pk_in_complaints(pk):
    """Метод вывода объектов всех ответов по конкретной жалобе на форуме"""
    question = ForumComplaints.objects.get(pk=pk)
    return ForumComplaintAnswer.objects.filter(question=question).order_by('-date')

def get_user_status_object(request):
    """Метод получения объекта User_Status для АВТОРИЗИРОВАННОГО пользователя"""
    return User_Status.objects.get(username=request.user)

def get_waiting_tickets():
    """Метод получения объектов всех не закрытых вопросов с форума"""
    all_waiting_tickets = ForumTechQuestions.objects.order_by('-date').filter(is_resolved=False)
    return all_waiting_tickets

def get_waiting_complates():
    """Метод получения объектов всех не закрытых жалоб с форума"""
    all_waiting_complates = ForumComplaints.objects.order_by('-date').filter(is_resolved=False)
    return all_waiting_complates

def get_closed_tickets():
    """Метод получения объектов всех закрытых вопросов с форума"""
    all_closed_tickets = ForumTechQuestions.objects.order_by('-date').filter(is_resolved=True)
    return all_closed_tickets

def get_closed_complaints():
    """Метод получения объектов всех закрытых жалоб с форума"""
    all_closed_complaints = ForumComplaints.objects.order_by('-date').filter(is_resolved=True)
    return all_closed_complaints

def get_user_tickets(request):
    """Метод получения всех объектов вопросов на форум АВТОРИЗИРОВАННОГО пользователя"""
    all_user_tickets = ForumTechQuestions.objects.filter(user=request.user).order_by('is_resolved')
    return all_user_tickets

def get_user_complaints(request):
    """Метод получения всех объектов жалоб на форум АВТОРИЗИРОВАННОГО пользователя"""
    all_user_complaints = ForumComplaints.objects.filter(user=request.user).order_by('is_resolved')
    return all_user_complaints

def get_record_for_pk(pk):
    """Метод получения объекта технического вопроса по его PK"""
    return ForumTechQuestions.objects.get(pk = pk)

def get_complaint_for_pk(pk):
    """Метод получения объекта жалобы по её PK"""
    return ForumComplaints.objects.get(pk=pk)

def get_user_status_object_for_pk_in_TechQuestions(pk):
    """Получение объекта User_Status пользователя, являющегося автором письма в тех поддержку с конкретным PK"""
    user = ForumTechQuestions.objects.get(pk=pk).user
    return User_Status.objects.get(username=user)

def get_user_status_object_for_pk_in_complaints(pk):
    """Получение объекта User_Status пользователя, являющегося автором жалобы с конкретным PK"""
    user = ForumComplaints.objects.get(pk=pk).user
    return User_Status.objects.get(username=user)

def get_stuff_users():
    """Метод получения объектов User_Status пользователей, являющийся персоналом проекта и их разделение на адм. и модер."""
    admins = User_Status.objects.filter(is_staff=True)
    moderators = User_Status.objects.filter(is_moderator=True)
    return {'admins':admins, 'moderators':moderators }

def get_public_messages():
    """Метод получения объектов всех сообщений общего чата"""
    return Public_Chat.objects.order_by('-date')


def save_message(request):
    """Метод сохранения формы отправки сообщений общего чата"""
    form= PublicMessageForm(request.POST)
    if form.is_valid():
        response = form.save(commit=False)
        response.username = User_Status.objects.get(username=request.user.id)
        response.save()
        form = PublicMessageForm()
    return form

def get_rich_users():
    """Метод получения объектов User_Status 3-х пользователей, имеющих самый большой баланс"""
    return User_Status.objects.order_by('-balance')[:3]