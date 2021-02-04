from django.shortcuts import render
from happyworld.models import Author
from django.http import HttpResponse
# Create your views here.


def home_page(request):
    authors_name = Author.objects.all()
    context = {"authors_name" : authors_name}
    return render(request, template_name='home.html', context=context)