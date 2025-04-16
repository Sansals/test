from .models import Public_Chat, ForumTechQuestions, ForumTechAnswer, ForumComplaints, ForumComplaintAnswer
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
            visible.field.widget.attrs['class'] = ('px-2 m-2 bg-gray-400 rounded-lg border-2 text-lg leading-relaxed border-gray-100'
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

class ForumComplaintsAnswerForm(ModelForm):
    class Meta:
        model = ForumComplaintAnswer
        fields = ['is_anonymous', 'answer']

        widgets = {
        'answer': TextInput(attrs={
            'class': 'h-15 bg-neutral-600 rounded-lg italic px-5 hover:border-green-600 hover:border-2',
            'placeholder': 'Введите сообщение'
        })
    }

class ForumComplaintsForm(ModelForm):
    class Meta:
        model = ForumComplaints
        fields = ['subject', 'defendant', 'question', 'proofs', 'is_anonymous']

    def __init__(self, *args, **kwargs):
        super(ForumComplaintsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = ('px-2 m-2 bg-gray-400 rounded-lg border-2 text-lg leading-relaxed border-gray-100'
                                                   ' focus:border-green-400')


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