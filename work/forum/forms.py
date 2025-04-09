from .models import Articles, Public_Chat, ForumTechQuestions, ForumTechAnswer
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from django import forms

class ForumTechSupportQuestionsForm(ModelForm):
    class Meta:
        model = ForumTechQuestions
        fields = ['subject', 'question', 'proofs']

    widgets = {
        'question': TextInput(attrs={
            'class': 'h-200',
            'placeholder': 'Введите сообщение'
        })
    }



    def __init__(self, *args, **kwargs):
        super(ForumTechSupportQuestionsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = ('m-2 bg-gray-400 rounded-lg border-2 text-lg leading-relaxed border-gray-100'
                                                   ' focus:border-green-400')

class ForumTechSupportAnswerForm(ModelForm):
    class Meta:
        model = ForumTechAnswer
        fields = ['is_anonymous', 'answer']

        widgets = {
        'answer': TextInput(attrs={
            'class': 'h-15 bg-neutral-600 rounded-lg italic px-5 hover:border-green-600 hover:border-2',
            'placeholder': 'Введите сообщение'
        })
    }

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