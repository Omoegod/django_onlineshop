from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, DeleteView, ListView, CreateView, UpdateView
from product.models import Product
from product import forms

# Create your views here.

class ProductList(ListView):
    model = Product

class ProductDetail(DetailView):
    model = Product

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('books-list')

class ProductCreate(CreateView):
    model = Product
    success_url = reverse_lazy('books-list')
    form_class = forms.ProductFormCreate
    template_name_suffix = '_create'

class ProductUpdate(UpdateView):
    model = Product   
    success_url = reverse_lazy('books-list')
    form_class = forms.ProductFormUpdate 
    template_name_suffix = '_update'