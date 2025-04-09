from .models import Articles, Public_Chat, ForumTechQuestions
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ForumTechSupportForm(ModelForm):
    class Meta:
        model = ForumTechQuestions
        fields = ['subject', 'question', 'proofs', 'is_resolved']




class PublicMessageForm(ModelForm):
    class Meta:
        model = Public_Chat
        fields = ['text']

        widgets = {
            'text': TextInput(attrs={
                'class': 'text-center w-full text-black text-xl border-2 rounded-lg border-indigo-900 '
                         'hover:border-black ',
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