from django import forms
from product.models import Product
from django.db.models import fields


class ProductFormCreate(forms.ModelForm):
    class Meta:
        model = Product
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

class ProductFormUpdate(forms.ModelForm):
    class Meta:
        model = Product
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