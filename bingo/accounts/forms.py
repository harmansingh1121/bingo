from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

# Registeration form

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'username']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class LoginForm(AuthenticationForm):

    class Meta:
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
