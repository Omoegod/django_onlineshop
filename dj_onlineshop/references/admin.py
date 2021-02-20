from django.contrib import admin
from references import models



class GenreAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name_genre',
        'descriptions_genre']

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
        'name_author',
        'descriptions_author']


admin.site.register(models.Genre, GenreAdmin)
admin.site.register(models.Series, SeriesAdmin)
admin.site.register(models.Publishing, PublishingAdmin)
admin.site.register(models.Author, AuthorAdmin)

