from django.contrib import admin
from happyworld import models

class BookAdmin(admin.ModelAdmin):
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
        'updated']

class GenreAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name_genre']

class SeriesAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name_series']

class PublishingAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name_publishing']

class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name_author']

admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Genre, GenreAdmin)
admin.site.register(models.Series, SeriesAdmin)
admin.site.register(models.Publishing, PublishingAdmin)
admin.site.register(models.Author, AuthorAdmin)

