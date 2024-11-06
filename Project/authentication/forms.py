from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class UserLoginForm(forms.Form):
    Username = forms.CharField()
    Password = forms.CharField(widget=forms.PasswordInput())


class UserRegistrationForm(UserCreationForm):
    class meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']