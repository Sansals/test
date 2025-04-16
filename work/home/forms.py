from .models import News_Comments
from django import forms
from django.forms import ModelForm, TextInput

class CommentsForm(ModelForm):
    class Meta:
        model = News_Comments
        fields = ['comment']

        widgets = {
            'comment': TextInput(attrs={
                'class': 'w-full text-black text-xl border-2 rounded-lg border-gray-500 '
                         'hover:border-black px-2 col-span-8',
                'placeholder': 'Введите комментарий'
            })
        }