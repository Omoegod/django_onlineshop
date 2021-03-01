from django import forms
from django.db.models import fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SingUpForm(UserCreationForm):
    password1 = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'})
        )
    password2 = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'})
        )   
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'            
        ]

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1'
        ]

                       
