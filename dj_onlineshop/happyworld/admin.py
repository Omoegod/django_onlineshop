from django.contrib import admin
from happyworld.models import reference



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


admin.site.register(reference.Genre, GenreAdmin)
admin.site.register(reference.Series, SeriesAdmin)
admin.site.register(reference.Publishing, PublishingAdmin)
admin.site.register(reference.Author, AuthorAdmin)

