from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from choices.models import Choice
from .models import User

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['title', 'description', 'preparation']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() #default required=True

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_picture']