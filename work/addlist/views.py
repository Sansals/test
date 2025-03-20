from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView
from django.contrib.auth.models import User

from login.models import User_Status


class NewsDatailView(DetailView):
    model = Articles
    template_name = 'addlist/details_view.html'
    context_object_name = 'article'


@ login_required
def createnews(request):
    error = ''
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        #form.user_id = User.objects.get(username=request.user.username).id
        #form.user_id = User.objects.get(username=request.user.username).id
        if form.is_valid():
            response = form.save(commit=False)
            response.username = request.user
            response.save()
        else:
            error = 'Не верно'


    form = ArticlesForm

    data ={
        'form': form,
        'error': error
    }
    return render(request, 'addlist/createnews.html', data)
