from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ArticlesForm, ForumTechSupportQuestionsForm, ForumTechSupportAnswerForm, ForumComplaintsForm, ForumComplaintsAnswerForm
from work.global_services import get_user

from .models import Public_Chat, ForumTechQuestions, ForumTechAnswer, ForumComplaints

from shop.services import basket_value
from .services import *
from work.global_services import get_username, get_user_verify_is
from login.services import save_verify_code
import logging
import datetime

logger = logging.getLogger(__name__)

def complaints_form_view(request):
    form = ForumComplaintsForm(request.POST)
    if form.is_valid():
        response = form.save(commit=False)
        response.user = request.user
        response.save()
        return redirect('complaints_waiting')
    data= {
        'form':form,
        'basket_value': basket_value(request),
    }
    return render(request, 'forum/complaints/form.html', data)

@login_required()
def techsupport_form_view(request):
    form = ForumTechSupportQuestionsForm(request.POST)
    if form.is_valid():
        response = form.save(commit=False)
        response.user = request.user
        response.save()
        return redirect('techsupport_waiting')
    data = {
        'form': form,
        'basket_value': basket_value(request),
    }
    return render(request, 'forum/techsupport/form.html', data)

def techsupport_closed_view(request):
    data = {
        'title_text': 'Закрытые обращения',
        'all_tickets': get_closed_tickets(),
        'basket_value': basket_value(request),
    }
    return render(request, 'forum/techsupport/records.html', data)

def complaints_closed_view(request):
    data = {
        'title_text': 'Закрытые жалобы',
        'all_tickets': get_closed_complaints(),
        'basket_value': basket_value(request),
    }
    return render(request, 'forum/complaints/records.html', data)

def techsupport_record_view(request, pk):
    form = ForumTechSupportAnswerForm(request.POST)
    if form.is_valid():
        response = form.save(commit=False)
        response.user = User.objects.get(username=request.user)
        response.question = ForumTechQuestions.objects.get(pk=pk)
        response.save()
        form = ForumTechSupportAnswerForm()
        logger.warning(
            f'response.question = {response.question}; response.user = {response.user}')
    data={
        'record': get_record_for_pk(pk),
        'user_status_object': get_user_status_object_for_pk(pk),
        'form_answer': form,
        'user_request_status_object': get_user_status_object(request),
        'answers':get_answers(pk),
        'basket_value': basket_value(request),
    }
    return render(request, 'forum/techsupport/record_view.html', data)

def complaints_record_view(request, pk):
    form = ForumComplaintsAnswerForm(request.POST)
    if form.is_valid():
        response = form.save(commit=False)
        response.user = User.objects.get(username=request.user)
        response.question = ForumComplaints.objects.get(pk=pk)
        response.save()
        form = ForumComplaintsAnswerForm()
        logger.warning(
            f'response.question = {response.question}; response.user = {response.user}')
    data = {
        'record': get_complaint_for_pk(pk),
        'user_status_object': get_user_status_object_for_pk_in_complaints(pk),
        'form_answer': form,
        'user_request_status_object': get_user_status_object(request),
        'answers': get_answers_for_pk_in_complaints(pk),
        'basket_value': basket_value(request),
    }
    return render(request, 'forum/complaints/record_view.html', data)

def techsupport_waiting_view(request):
    data= {
        'title_text':'Ожидающие обращения',
        'all_tickets': get_waiting_tickets(),
        'basket_value': basket_value(request),
    }
    return render(request, 'forum/techsupport/records.html', data)

def complaints_waiting_view(request):
    data = {
        'title_text': 'Жалобы ожидающие рассмотрения',
        'all_tickets': get_waiting_complates(),
        'basket_value': basket_value(request),
    }
    return render(request, 'forum/complaints/records.html', data)

def techsupport_user_tickets_view(request):
    data = {
        'title_text': 'Мои обращения',
        'all_tickets': get_user_tickets(request),
        'basket_value': basket_value(request),
    }
    return render(request, 'forum/techsupport/records.html', data)

def complaints_user_tickets_view(request):
    data = {
        'title_text': 'Мои обращения',
        'all_tickets': get_user_complaints(request),
        'basket_value': basket_value(request),
    }
    return render(request, 'forum/complaints/records.html', data)

@login_required()
def forum_view(request):
    data ={
        'username': get_username(request),
        'rich_users_top': get_rich_users(),
        'message_input': save_message(request),
        'all_messages': get_public_messages,
        'stuff_users': get_stuff_users,
        'basket_value': basket_value(request)
    }
    return render(request, 'forum/forum_index.html', data)
