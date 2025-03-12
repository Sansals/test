from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm


def addlist(request):
    news = Articles.objects.order_by('date')
    return render(request, 'addlist/addlist.html', {'news': news})

def createnews(request):
    error = ''
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Не верно'


    form = ArticlesForm

    data ={
        'form': form,
        'error': error
    }
    return render(request, 'addlist/createnews.html', data)
