from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, DeleteView, ListView, CreateView, TemplateView, UpdateView
from django.contrib.auth.views import LoginView
from happyworld import forms
from happyworld.models.reference import Author, Genre 
from happyworld.models.users import User


# Create your views here.

class HomePage(TemplateView):
    template_name = 'home.html'

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

class GenreList(ListView):
    model = Genre

class GenreDetail(DetailView):
    model = Genre

class GenreDelete(DeleteView):
    model = Genre
    success_url = reverse_lazy('genres-list')

class GenreCreate(CreateView):
    model = Genre
    success_url = reverse_lazy('genres-list')
    form_class = forms.GenreFormCreate
    template_name_suffix = '_create'

class GenreUpdate(UpdateView):
    model = Genre   
    success_url = reverse_lazy('genres-list')
    form_class = forms.GenreFormUpdate 
    template_name_suffix = '_update'

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
   
    