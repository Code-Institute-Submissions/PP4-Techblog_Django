from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import RegistrationForm


class UserRegisterView(generic.CreateView):
    form_class = RegistrationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')

class UserUpdateView(generic.CreateView):
    form_class = UserChangeForm
    template_name = 'registration/update_profile.html'
    success_url = reverse_lazy('home')