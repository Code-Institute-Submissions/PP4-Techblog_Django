from django.urls import path
from .views import UserRegisterView, UserUpdateView, ProfilePageView, EditProfilePageView, CreateProfilePageView
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('register/', UserRegisterView.as_view(), name='registration'),
   path('update_profile/', UserUpdateView.as_view(), name='update_profile'),
   path('<int:pk>/profile/', ProfilePageView.as_view(), name='show_profile_page'),
   path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
   path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),
   path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
]
