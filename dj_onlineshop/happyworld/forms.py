from django import forms
from happyworld import models
from django.db.models import fields

class BookFormCreate(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = [
            'name_book',
            'descriptions_book', 
            'author_book', 
            'genre_book', 
            'series_book', 
            'publishing_book', 
            'year_publishing', 
            'number_of_pages'
            ]

class BookFormUpdate(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = [
            'name_book',
            'descriptions_book', 
            'author_book', 
            'genre_book', 
            'series_book', 
            'publishing_book', 
            'year_publishing', 
            'number_of_pages'
            ]
                        
class AuthorFormCreate(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = [
            'name_author',
            'descriptions_author', 
            ]

class AuthorFormUpdate(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = [
            'name_author',
            'descriptions_author', 
            ]

class GenreFormCreate(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = [
            'name_genre',
            'descriptions_genre', 
            ]

class GenreFormUpdate(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = [
            'name_genre',
            'descriptions_genre', 
            ]