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
from django.urls import path
from product import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('books/', views.ProductList.as_view(), name='books-list'),
    path('books/<int:pk>/', views.ProductDetail.as_view(), name='book-detail'),
    path('book-delete/<int:pk>/', views.ProductDelete.as_view(), name='book-delete'),
    path('book-update/<int:pk>/', views.ProductUpdate.as_view(), name='book-update'),
    path('book-create/', views.ProductCreate.as_view(), name='book-create'),
    path('catalogue/', views.Catalogue.as_view(), name='catalogue'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
