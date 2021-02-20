from django import forms
from references.models import Author, Genre
from django.db.models import fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SingUpForm(UserCreationForm):
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

                       
class AuthorFormCreate(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'name_author',
            'descriptions_author', 
            ]

class AuthorFormUpdate(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'name_author',
            'descriptions_author', 
            ]

class GenreFormCreate(forms.ModelForm):
    class Meta:
        model = Genre
        fields = [
            'name_genre',
            'descriptions_genre', 
            ]

class GenreFormUpdate(forms.ModelForm):
    class Meta:
        model = Genre
        fields = [
            'name_genre',
            'descriptions_genre', 
            ]