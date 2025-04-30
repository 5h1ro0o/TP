from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Participation

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ParticipationForm(forms.ModelForm):
    class Meta:
        model = Participation
        fields = ['is_attending']
        labels = {
            'is_attending': 'Je participe à cet événement'
        }