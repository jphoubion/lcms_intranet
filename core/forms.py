from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Nom d'utilisateur",
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Adresse email",
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Mot de passe",
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Répétez le mot de passe",
        'class': 'w-full py-4 px-6 rounded-xl'
    }))