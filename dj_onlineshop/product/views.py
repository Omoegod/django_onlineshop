from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, DeleteView, ListView, CreateView, UpdateView
from product.models import Product
from product import forms
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.

class ProductList(ListView):
    model = Product
    paginate_by = 20

class ProductDetail(DetailView):
    model = Product

class ProductDelete(PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('books-list')
    permission_required = 'product.delete_product'  
    login_url = '/login/'

class ProductCreate(PermissionRequiredMixin, CreateView):
    model = Product
    success_url = reverse_lazy('books-list')
    form_class = forms.ProductFormCreate
    template_name_suffix = '_create'
    permission_required = 'product.add_product'  
    login_url = '/login/'

class ProductUpdate(PermissionRequiredMixin, UpdateView):
    model = Product   
    success_url = reverse_lazy('books-list')
    form_class = forms.ProductFormUpdate 
    template_name_suffix = '_update'
    permission_required = 'product.change_product'  
    login_url = '/login/'

class Catalogue(ListView):
    model = Product
    template_name_suffix = '_catalogue'
    paginate_by = 20 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = 'catalogue'
        return context
    