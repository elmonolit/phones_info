from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=False)
    class Meta:
        model = User
        fields = ('username', 'password1','password2','email')

# class SignIn()