from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField("Name author", max_length=30)
    descriptions = models.CharField("Descriptions Author", max_length=200)
    
    def __str__(self):
        return self.name

class Genre(models.Model):
    name_genre = models.CharField("Name genre", max_length=30)
    
    def __str__(self):
        return self.name_genre
        
class Series(models.Model):
    name_series = models.CharField("Name series", max_length=30)

    def __str__(self):
        return self.name_series

class Publishing(models.Model):
    name_publishing = models.CharField("Name publishing house", max_length=50)

    def __str__(self):
        return self.name_publishing