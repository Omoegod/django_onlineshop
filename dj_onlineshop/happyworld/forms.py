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
                        