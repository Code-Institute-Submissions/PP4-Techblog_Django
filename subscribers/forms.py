from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from blog.models import UserProfile

class ProfilePageForm(forms.ModelForm):
    model = UserProfile
    field = ('bio', 'avatar', 'website_url', 'instagram_url', 'twitter_url', 'linkedin_url')
    widgets = {
        'bio': forms.Textarea(attrs={'class': 'form-control'}),
        # 'avatar': forms.TextInput(attrs={'class': 'form-control'}),
        'website_url': forms.TextInput(attrs={'class': 'form-control'}),
        'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
        'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
        'linkedin_url': forms.TextInput(attrs={'class': 'form-control'}),
    }


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class UpdateProfileForm(UserChangeForm):
    first_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_joined = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'last_login', 'date_joined')