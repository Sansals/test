from django import forms
from login.models import User_Status

class AvatarUpdateForm(forms.ModelForm):
    class Meta:
        model = User_Status
        fields = ['avatar']