from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from profiles import models, forms
from order.models import Order
from proj import settings
# Create your views here.


class SignUpView(CreateView):
    model = models.User
    form_class = forms.SingUpForm
    success_url = reverse_lazy('home')
    template_name = 'register.html'

class Login(LoginView):
    model = models.User
    form_class = forms.LoginForm
    success_url = reverse_lazy('home')
    template_name = 'login.html'

class Logout_view(LogoutView):
    redirect_field_name = settings.LOGOUT_REDIRECT_URL

class ProfileDetail(LoginRequiredMixin, DetailView):
    template_name = 'profiles/account_detail.html'
    queryset = models.Profile.objects.all()
    
class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = models.Profile
    template_name = 'profiles/account_update.html'
    success_url = reverse_lazy('home')
    form_class = forms.ProfileUpdate

