from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ForumTechSupportQuestionsForm, ForumTechSupportAnswerForm, ForumComplaintsForm, ForumComplaintsAnswerForm
from work.global_services import get_user

from .models import Public_Chat, ForumTechQuestions, ForumTechAnswer, ForumComplaints

from shop.services import basket_value
from .services import *


@login_required()
def complaints_form_view(request):
    """Метод представления формы подачи жалоб"""
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
    """Метод представления формы подачи письма в техподдержку"""
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

@login_required()
def techsupport_closed_view(request):
    """Метод представления закрытых обращений в тех. поддержку"""
    data = {
        'title_text': 'Закрытые обращения',
        'all_tickets': get_closed_tickets(),
        'basket_value': basket_value(request),
    }
    return render(request, 'forum/techsupport/records.html', data)

@login_required()
def complaints_closed_view(request):
    """Метод представления закрытых жалоб"""
    data = {
        'title_text': 'Закрытые жалобы',
        'all_tickets': get_closed_complaints(),
        'basket_value': basket_value(request),
    }
    return render(request, 'forum/complaints/records.html', data)

@login_required()
def techsupport_record_view(request, pk):
    """Метод представления письма в тех. поддержку"""
    form = ForumTechSupportAnswerForm(request.POST)
    if form.is_valid():
        response = form.save(commit=False)
        response.user = User_Status.objects.get(username=request.user.id)
        response.question = ForumTechQuestions.objects.get(pk=pk)
        response.save()
        form = ForumTechSupportAnswerForm()
    data={
        'record': get_record_for_pk(pk),
        'user_status_object': get_user_status_object_for_pk_in_TechQuestions(pk),
        'form_answer': form,
        'user_request_status_object': get_user_status_object(request),
        'answers':get_answers(pk),
        'basket_value': basket_value(request),
    }
    return render(request, 'forum/techsupport/record_view.html', data)

@login_required()
def complaints_record_view(request, pk):
    """Метод представления жалобы"""
    form = ForumComplaintsAnswerForm(request.POST)
    if form.is_valid():
        response = form.save(commit=False)
        response.user = User_Status.objects.get(username=request.user.id)
        response.question = ForumComplaints.objects.get(pk=pk)
        response.save()
        form = ForumComplaintsAnswerForm()
    data = {
        'record': get_complaint_for_pk(pk),
        'user_status_object': get_user_status_object_for_pk_in_complaints(pk),
        'form_answer': form,
        'user_request_status_object': get_user_status_object(request),
        'answers': get_answers_for_pk_in_complaints(pk),
        'basket_value': basket_value(request),
    }
    return render(request, 'forum/complaints/record_view.html', data)

@login_required()
def techsupport_waiting_view(request):
    """Метод представления ожидающих ответа вопросов в тех поддержку"""
    data= {
        'title_text':'Ожидающие обращения',
        'all_tickets': get_waiting_tickets(),
        'basket_value': basket_value(request),
    }
    return render(request, 'forum/techsupport/records.html', data)

@login_required()
def complaints_waiting_view(request):
    """Метод представления ожидающих ответа жалоб"""
    data = {
        'title_text': 'Жалобы ожидающие рассмотрения',
        'all_tickets': get_waiting_complates(),
        'basket_value': basket_value(request),
    }
    return render(request, 'forum/complaints/records.html', data)

@login_required()
def techsupport_user_tickets_view(request):
    """Метод представления писем в тех поддержку для конкретного пользователя"""
    data = {
        'title_text': 'Мои обращения',
        'all_tickets': get_user_tickets(request),
        'basket_value': basket_value(request),
    }
    return render(request, 'forum/techsupport/records.html', data)

@login_required()
def complaints_user_tickets_view(request):
    """Метод представления жалоб для конкретного пользователя"""
    data = {
        'title_text': 'Мои обращения',
        'all_tickets': get_user_complaints(request),
        'basket_value': basket_value(request),
    }
    return render(request, 'forum/complaints/records.html', data)

@login_required()
def forum_view(request):
    """Метод представления главной страницы форума"""
    data ={
        'rich_users_top': get_rich_users(),
        'message_input': save_message(request),
        'all_messages': get_public_messages,
        'stuff_users': get_stuff_users,
        'basket_value': basket_value(request),
        'complaints_len': get_complaints_len(),
        'questions_len': get_questions_len(),
    }
    return render(request, 'forum/forum_index.html', data)
