from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, DeleteView, ListView, CreateView, TemplateView, UpdateView
from happyworld import forms
from happyworld.models import *

# Create your views here.

class HomePage(TemplateView):
    template_name = 'home.html'

class BookList(ListView):
    model = Book

class BookDetail(DetailView):
    model = Book

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books-list')

class BookCreate(CreateView):
    model = Book
    success_url = reverse_lazy('books-list')
    form_class = forms.BookFormCreate
    template_name_suffix = '_create'

class BookUpdate(UpdateView):
    model = Book   
    success_url = reverse_lazy('books-list')
    form_class = forms.BookFormUpdate 
    template_name_suffix = '_update'

class AuthorList(ListView):
    model = Author

class AuthorDetail(DetailView):
    model = Author

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors-list')

class AuthorCreate(CreateView):
    model = Author
    success_url = reverse_lazy('authors-list')
    form_class = forms.AuthorFormCreate
    template_name_suffix = '_create'

class AuthorUpdate(UpdateView):
    model = Author   
    success_url = reverse_lazy('authors-list')
    form_class = forms.AuthorFormUpdate 
    template_name_suffix = '_update'


