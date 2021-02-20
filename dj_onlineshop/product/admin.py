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
        'descriptions_book',
        'author_book',
        'genre_book',
        'series_book',
        'publishing_book',
        'year_publishing',
        'number_of_pages',
        'created',
        'updated',] 
    class Meta:
        model = Product           

class ProductImageAdmin(admin.ModelAdmin):
    list_display =[
        'pk',
        'product',
        'image',
        'created',
        'updated']    
    class Meta:
        model = ProductsImage   


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductsImage, ProductImageAdmin)



