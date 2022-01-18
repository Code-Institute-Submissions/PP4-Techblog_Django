from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import RegistrationForm, UpdateProfileForm
from blog.models import UserProfile


class EditProfilePageView(generic.UpdateView):
    model = UserProfile
    template_name = 'registration/edit_profile_page.html'


class ProfilePageView(DetailView):
    model = UserProfile
    template_name = 'registration/user_profile.html'
    
    def get_context_data(self, *args, **kwargs):
        users = UserProfile.objects.all()
        context = super(ProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context



class UserRegisterView(generic.CreateView):
    form_class = RegistrationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')

class UserUpdateView(generic.UpdateView):
    form_class = UpdateProfileForm
    template_name = 'registration/update_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

