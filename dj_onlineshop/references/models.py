from django.db import models

# Create your models here.
class Author(models.Model):
    name_author = models.CharField(
        verbose_name="Name author", 
        max_length=30)
    descriptions_author = models.TextField(
        verbose_name="Descriptions Author",
        null=True, 
        blank=True)
    
    def __str__(self):
        return f'{self.name_author}'

class Genre(models.Model):
    name_genre = models.CharField(
        verbose_name="Name genre", 
        max_length=50)
    descriptions_genre = models.TextField(
        verbose_name="Descriptions Author",
        null=True, 
        blank=True)    
    
    def __str__(self):
        return f'{self.name_genre}'
        
class Series(models.Model):
    name_series = models.CharField(
        verbose_name="Name series", 
        max_length=50)

    def __str__(self):
        return self.name_series

class Publishing(models.Model):
    name_publishing = models.CharField(
        verbose_name="Name publishing house",
        max_length=50)

    def __str__(self):
        return self.name_publishing

