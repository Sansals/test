from .models import Articles, Public_Chat
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class PublicMessageForm(ModelForm):
    class Meta:
        model = Public_Chat
        fields = ['text']

        widgets = {
            'text': TextInput(attrs={
                'class': 'message-input',
                'placeholder': 'Введите сообщение'
            })
        }

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),

        }