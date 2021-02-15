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

class Book(models.Model):
    name_book = models.CharField(
        verbose_name="Name book", 
        max_length=100)
    descriptions_book = models.TextField(
        verbose_name="Descriptions book",
        max_length=1000,
        null=True, 
        blank=True)     
    author_book = models.ForeignKey(
        'happyworld.Author',
        on_delete=models.PROTECT,
        verbose_name="Author",
        blank=True,
        null=True)
    genre_book = models.ForeignKey(
        'happyworld.Genre',
        on_delete=models.PROTECT,
        verbose_name="Genre",
        blank=True,
        null=True)
    series_book = models.ForeignKey(
        'happyworld.Series',
        on_delete=models.PROTECT,
        verbose_name="Series",
        blank=True,
        null=True)
    publishing_book = models.ForeignKey(
        'happyworld.Publishing',
        on_delete=models.PROTECT,
        verbose_name="Publishing",
        blank=True,
        null=True)
    year_publishing = models.PositiveSmallIntegerField(
        verbose_name="Year publishing",
        blank=True,
        null=True)
    number_of_pages = models.PositiveSmallIntegerField(
        verbose_name="Number of page",
        blank=True,
        null=True)    
    created = models.DateTimeField(
        verbose_name="Created date",
        auto_now=True,
        auto_now_add=False)
    updated = models.DateTimeField(
        verbose_name="Updated date",
        auto_now=False,
        auto_now_add=True)
    
    def __str__(self):
        return f'{self.name_book} {self.author_book} {self.genre_book} {self.series_book} {self.publishing_book}'
           