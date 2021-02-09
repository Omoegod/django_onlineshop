from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, DeleteView, ListView, CreateView, TemplateView, UpdateView
from happyworld import forms
from happyworld.models import Book, Author
# Create your views here.

class HomePage(TemplateView):
    template_name = 'home.html'
# def home_page(request):
#     authors_name = Author.objects.all()
#     context = {"authors_name" : authors_name}
#     return render(request, template_name='home.html', context=context)

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
    template_name = 'book_form_create.html'
    
class BookUpdate(UpdateView):
    model = Book   
    success_url = reverse_lazy('books-list')
    form_class = forms.BookFormUpdate 
    template_name = 'book_form_update.html'

