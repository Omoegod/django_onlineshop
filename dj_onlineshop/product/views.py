from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, DeleteView, ListView, CreateView, UpdateView
from product.models import Product
from product import forms
from django.contrib.auth.mixins import PermissionRequiredMixin
from references.models import Author
# Create your views here.

class ProductList(ListView):
    model = Product
    paginate_by = 9
    

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
    

class FilterProduct(DetailView):
    model = Product
    template_name = 'product/product_filter_genre.html'

    def get(self, request):
        genre_id = self.request.GET.get('genre')
        sort_genre = Product.objects.filter(genre_book=genre_id)   
        context = {
            'sort_genre':sort_genre,            
        }   
        return render(request, self.template_name, context)

class FilterAuthor(DetailView):
    model = Product
    template_name = 'references/author_filter.html'

    def get(self, request):
        author_id = self.request.GET.get('author')
        sort_author = Product.objects.filter(author_book=author_id)   
        context = {
            'sort_author':sort_author,            
        }   
        return render(request, self.template_name, context)    


    