from django.shortcuts import render
from happyworld.models import Book, Author
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def home_page(request):
    authors_name = Author.objects.all()
    context = {"authors_name" : authors_name}
    return render(request, template_name='home.html', context=context)

def book_list(request):
    name_book = Book.objects.all()
    context = {"name_book" : name_book}
    return render(request, template_name='books.html', context=context)

def books_detail(request, pk):
    book = Book.objects.get(pk=pk)
    context = {"object" : book}
    return render(request, template_name='book-detail.html', context=context)

def books_delete(request, pk):
    book = Book.objects.get(pk=pk)
    message = f'Book {book.name_book} has just been deleted!!!'
    book.delete()
    context = {"message" : message}
    return render(request, template_name='delete.html', context=context)

def book_create(request):
    if request.method == "POST":
        name = request.POST.get('name_book')
        descriptions = request.POST.get('descriptions_book')
        book = Book.objects.create(name_book=name, descriptions_book=descriptions)
        return HttpResponseRedirect(reverse('book-detail', kwargs={'pk':book.pk}))
    context = {}
    return render(request, template_name='create.html', context=context)
