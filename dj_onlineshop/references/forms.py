from django import forms
from references.models import Author, Genre
from django.db.models import fields


                       
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