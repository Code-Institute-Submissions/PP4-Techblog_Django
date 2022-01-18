from django.urls import path
from .views import UserRegisterView, UserUpdateView, ProfilePageView

urlpatterns = [
   path('register/', UserRegisterView.as_view(), name='registration'),
   path('update_profile/', UserUpdateView.as_view(), name='update_profile'),
   path('<int:pk>/profile/', ProfilePageView.as_view(), name='show_profile_page'),
]
