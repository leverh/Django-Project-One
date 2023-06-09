from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Choice
from cloudinary.forms import CloudinaryFileField

class ChoiceForm(forms.ModelForm):
    picture = CloudinaryFileField()
    class Meta:
        model = Choice
        fields = ['title', 'description', 'preparation', 'picture']

def clean_picture(self):
        picture = self.cleaned_data.get('picture')
        if picture:
            pass
        return picture


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # default required=True

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
