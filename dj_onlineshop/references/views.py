from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, DeleteView, ListView, CreateView, TemplateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import PermissionRequiredMixin
from references import forms
from references.models import Author, Genre 
from references.users import User


# Create your views here.

class HomePage(TemplateView):
    template_name = 'home.html'

class AuthorList(ListView):
    model = Author

class AuthorDetail(DetailView):
    model = Author

class AuthorDelete(PermissionRequiredMixin, DeleteView):
    model = Author
    permission_required = 'references.delete_author'  
    login_url = '/login/'
    success_url = reverse_lazy('authors-list')

class AuthorCreate(PermissionRequiredMixin, CreateView):
    model = Author
    success_url = reverse_lazy('authors-list')
    form_class = forms.AuthorFormCreate
    template_name_suffix = '_create'
    login_url = '/login/'
    permission_required = 'references.add_author'  


class AuthorUpdate(PermissionRequiredMixin, UpdateView):
    model = Author   
    success_url = reverse_lazy('authors-list')
    form_class = forms.AuthorFormUpdate 
    template_name_suffix = '_update'
    login_url = '/login/'
    permission_required = 'references.change_author'  


class GenreList(ListView):
    model = Genre

class GenreDetail(DetailView):
    model = Genre

class GenreDelete(PermissionRequiredMixin, DeleteView):
    model = Genre
    success_url = reverse_lazy('genres-list')
    login_url = '/login/'
    permission_required = 'references.delete_author'  

class GenreCreate(PermissionRequiredMixin, CreateView):
    model = Genre
    success_url = reverse_lazy('genres-list')
    form_class = forms.GenreFormCreate
    template_name_suffix = '_create'
    login_url = '/login/'
    permission_required = 'references.add_author'  

class GenreUpdate(PermissionRequiredMixin, UpdateView):
    model = Genre   
    success_url = reverse_lazy('genres-list')
    form_class = forms.GenreFormUpdate 
    template_name_suffix = '_update'
    login_url = '/login/'
    permission_required = 'references.change_author'  

class SignUpView(CreateView):
    model = User
    form_class = forms.SingUpForm
    success_url = reverse_lazy('home')
    template_name = 'register.html'

class Login(LoginView):
    model = User
    form_class = forms.LoginForm
    success_url = reverse_lazy('home')
    template_name = 'login.html'

class ProfileDetail(DetailView):
    model = User
    template_name = 'account_detail.html'
    def get_object(self, queryset=None):
        return self.request.user
   
    