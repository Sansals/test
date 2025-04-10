from .models import Articles, Public_Chat, ForumTechQuestions, ForumTechAnswer, ForumComplaints, ForumComplaintAnswer
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

def get_answers(pk):
    question = ForumTechQuestions.objects.get(pk=pk)
    return ForumTechAnswer.objects.filter(question=question).order_by('-date')

def get_answers_for_pk_in_complaints(pk):
    question = ForumComplaints.objects.get(pk=pk)
    return ForumComplaintAnswer.objects.filter(question=question).order_by('-date')

def get_user_status_object(request):
    return User_Status.objects.get(username=request.user)

def get_waiting_tickets():
    all_waiting_tickets = ForumTechQuestions.objects.order_by('-date').filter(is_resolved=False)
    return all_waiting_tickets

def get_waiting_complates():
    all_waiting_complates = ForumComplaints.objects.order_by('-date').filter(is_resolved=False)
    return all_waiting_complates

def get_closed_tickets():
    all_closed_tickets = ForumTechQuestions.objects.order_by('-date').filter(is_resolved=True)
    return all_closed_tickets

def get_closed_complaints():
    all_closed_complaints = ForumComplaints.objects.order_by('-date').filter(is_resolved=True)
    return all_closed_complaints

def get_user_tickets(request):
    all_user_tickets = ForumTechQuestions.objects.filter(user=request.user).order_by('is_resolved')
    return all_user_tickets

def get_user_complaints(request):
    all_user_complaints = ForumComplaints.objects.filter(user=request.user).order_by('is_resolved')
    return all_user_complaints

def get_record_for_pk(pk):
    return ForumTechQuestions.objects.get(pk = pk)

def get_complaint_for_pk(pk):
    return ForumComplaints.objects.get(pk=pk)

def get_user_status_object_for_pk(pk):
    user = ForumTechQuestions.objects.get(pk=pk).user
    return User_Status.objects.get(username=user)

def get_user_status_object_for_pk_in_complaints(pk):
    user = ForumComplaints.objects.get(pk=pk).user
    return User_Status.objects.get(username=user)

def get_stuff_users():
    admins = User_Status.objects.filter(is_staff=True)
    moderators = User_Status.objects.filter(is_moderator=True)
    return {'admins':admins, 'moderators':moderators }

def get_public_messages():
    return Public_Chat.objects.order_by('-date')


def save_message(request):
    form= PublicMessageForm()
    if request.method == "POST":
        if form.is_valid():
            response = form.save(commit=False)
            response.username = User_Status.objects.get(username=request.user.id)
            response.save()
            form = PublicMessageForm()
    return form

def get_rich_users():
    return User_Status.objects.order_by('-balance')[:3]


logger = logging.getLogger(__name__)

class ArticlesDatailView(DetailView):
    try:
        model = Articles
        template_name = 'forum/details_view.html'
        context_object_name = 'article'
    except ValueError:
        logger.warning(f'{datetime.datetime.now()} Не удалось получить объекты/объекты отсутствуют в addlist.Articles')
    except Exception:
        logger.error(f'{datetime.datetime.now()} Неизвестная ошибка при работе с addlist.Articles. Файл addlist.services')