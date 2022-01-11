from django.urls import path
from .views import UserRegisterView, UserUpdateView

urlpatterns = [
   path('register/', UserRegisterView.as_view(), name='registration'),
   path('update_profile/', UserUpdateView.as_view(), name='update_profile'),
]
