from django import forms
from happyworld.models import reference, users
from django.db.models import fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# class SingUpForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'first_name',
#             'last_name',
#             'email',
#             'password1',
#             'password2'            
#         ]

# class LoginForm(AuthenticationForm):
#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'password1'
#         ]

# class BookFormCreate(forms.ModelForm):
#     class Meta:
#         model = reference.Book
#         fields = [
#             'name_book',
#             'descriptions_book', 
#             'author_book', 
#             'genre_book', 
#             'series_book', 
#             'publishing_book', 
#             'year_publishing', 
#             'number_of_pages'
#             ]

# class BookFormUpdate(forms.ModelForm):
#     class Meta:
#         model = reference.Book
#         fields = [
#             'name_book',
#             'descriptions_book', 
#             'author_book', 
#             'genre_book', 
#             'series_book', 
#             'publishing_book', 
#             'year_publishing', 
#             'number_of_pages'
#             ]
                        
# class AuthorFormCreate(forms.ModelForm):
#     class Meta:
#         model = reference.Author
#         fields = [
#             'name_author',
#             'descriptions_author', 
#             ]

# class AuthorFormUpdate(forms.ModelForm):
#     class Meta:
#         model = reference.Author
#         fields = [
#             'name_author',
#             'descriptions_author', 
#             ]

# class GenreFormCreate(forms.ModelForm):
#     class Meta:
#         model = reference.Genre
#         fields = [
#             'name_genre',
#             'descriptions_genre', 
#             ]

# class GenreFormUpdate(forms.ModelForm):
#     class Meta:
#         model = reference.Genre
#         fields = [
#             'name_genre',
#             'descriptions_genre', 
#             ]