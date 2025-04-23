from django.contrib.auth.models import User
from django.views.generic import DetailView
import logging
import datetime
from itertools import chain
from .forms import AvatarUpdateForm
from home.models import News_Comments
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin
from login.models import User_Status
from work.global_services import *
from login.services import save_verify_code
from forum.models import ForumTechQuestions, ForumComplaints, ForumTechAnswer, ForumComplaintAnswer
from django.urls import reverse_lazy

def get_all_open_user_articles(url_username):
    user = User.objects.get(username=url_username)
    user_tech_open_questions = ForumTechQuestions.objects.filter(user=user, is_resolved = False).order_by('-date')
    user_forum_open_complaints = ForumComplaints.objects.filter(user=user, is_resolved = False).order_by('-date')
    all_open_user_articles = list(chain(user_forum_open_complaints, user_tech_open_questions))
    return all_open_user_articles

def get_all_user_answers(url_username):
    user_id = User.objects.get(username=url_username).id
    user = User_Status.objects.get(username=user_id)
    user_tech_answers = ForumTechAnswer.objects.filter(user=user).order_by('-date')
    user_forum_answers = ForumComplaintAnswer.objects.filter(user=user).order_by('-date')
    all_user_answers = list(chain(user_forum_answers, user_tech_answers))
    return all_user_answers

def get_all_closed_user_articles(url_username):
    user = User.objects.get(username=url_username)
    user_tech_closed_questions = ForumTechQuestions.objects.filter(user=user, is_resolved=True).order_by('-date')
    user_forum_closed_complaints = ForumComplaints.objects.filter(user=user, is_resolved=True).order_by('-date')
    all_closed_user_articles = list(chain(user_forum_closed_complaints, user_tech_closed_questions))
    return all_closed_user_articles

def get_all_user_comments(url_username):
    user = User.objects.get(username=url_username).id
    user_status = User_Status.objects.get(username=user)
    return News_Comments.objects.filter(user = user_status).order_by('-date')

def get_value_user_articles(url_username):
    user = User.objects.get(username = url_username)
    user_tech_questions = ForumTechQuestions.objects.filter(user = user)
    user_forum_complaints = ForumComplaints.objects.filter(user = user)
    value_of_all_user_articles = len(user_tech_questions) + len(user_forum_complaints)
    return value_of_all_user_articles

def get_value_user_answer(url_username):
    user_id = User.objects.get(username=url_username).id
    user = User_Status.objects.get(username=user_id)
    user_tech_answers = ForumTechAnswer.objects.filter(user=user)
    user_forum_complaints_answers = ForumComplaintAnswer.objects.filter(user=user)
    value_of_all_user_answers = len(user_tech_answers) + len(user_forum_complaints_answers)
    return value_of_all_user_answers

def get_value_user_comments(url_username):
    user = User.objects.get(username=url_username).id
    user_status = User_Status.objects.get(username = user)
    value_user_comments = len(News_Comments.objects.filter(user=user_status))
    return value_user_comments

def verification_email():
    save_verify_code(request)
    redirect('vrmail')

def get_user_profile_object(username):
    return User.objects.get(username=username)

def get_user_status_profile_object(username):
    user = User.objects.get(username=username)
    return User_Status.objects.get(username=user)

def get_object_from_user_status(request):
    user_object = User_Status.objects.get(username = get_user(request))
    return user_object

class AvatarUpdateView(UserPassesTestMixin, UpdateView):

    def test_func(self):
        if (self.request.user.id == self.get_object().username.id
            or self.request.user.is_staff):
            return True

    model = User_Status
    template_name = 'profiles/avatar_update.html'
    form_class = AvatarUpdateForm
    success_url = reverse_lazy('forum')