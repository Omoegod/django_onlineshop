"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from happyworld import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='home'),
    path('', include('product.urls')),
    path('authors/', views.AuthorList.as_view(), name='authors-list'),
    path('author/<int:pk>/', views.AuthorDetail.as_view(), name='author-detail'),
    path('author-delete/<int:pk>/', views.AuthorDelete.as_view(), name='author-delete'),
    path('author-update/<int:pk>/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author-create/', views.AuthorCreate.as_view(), name='author-create'),
    path('genres/', views.GenreList.as_view(), name='genres-list'),
    path('genre/<int:pk>/', views.GenreDetail.as_view(), name='genre-detail'),
    path('genre-delete/<int:pk>/', views.GenreDelete.as_view(), name='genre-delete'),
    path('genre-update/<int:pk>/', views.GenreUpdate.as_view(), name='genre-update'),
    path('genre-create/', views.GenreCreate.as_view(), name='genre-create'),
    path('register/', views.SignUpView.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('user/', views.ProfileDetail.as_view(), name='profile'),
]
