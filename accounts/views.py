from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import SignUpForm
from django.urls import reverse_lazy

class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'accounts/sign_up.html'
    success_url = reverse_lazy('sign_in')

class SignIn(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('index')
class Exit(LogoutView):
    next_page = reverse_lazy('index')