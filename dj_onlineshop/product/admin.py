from django.contrib import admin
from product.models import *

class ProductAdmin(admin.ModelAdmin):
    search_fields = [
        'name_book',
        'author_book__name_author',
        'genre_book__name_genre',
        'year_publishing']
    list_display = [
        'pk',
        'name_book',
        'photo',
        'price',
        'descriptions_book',
        'author_book',
        'genre_book',
        'series_book',
        'publishing_book',
        'year_publishing',
        'number_of_pages',
        'binding',
        'format_book',
        'isbn',
        'weight',
        'age_restrictions',
        'availability',
        'quantity',
        'created',
        'updated',] 
    class Meta:
        model = Product           
  


admin.site.register(Product, ProductAdmin)



