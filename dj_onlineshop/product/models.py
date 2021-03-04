from django.db import models


class Product(models.Model):
    name_book = models.CharField(
        verbose_name="Название книги", 
        max_length=100)
    photo = models.ImageField(
        verbose_name="Фотография",
        upload_to='uploads/',
        blank=True,
        max_length=200)        
    price = models.DecimalField(
        verbose_name="Цена",
        max_digits=6,
        decimal_places=2,
        default=0,
        blank=True)    
    descriptions_book = models.TextField(
        verbose_name="Описание книги",
        max_length=1000,
        null=True, 
        blank=True)     
    author_book = models.ForeignKey(
        'references.Author',
        on_delete=models.PROTECT,
        verbose_name="Автор",
        blank=True,
        null=True)
    genre_book = models.ForeignKey(
        'references.Genre',
        on_delete=models.PROTECT,
        verbose_name="Жанр",
        blank=True,
        null=True)
    series_book = models.ForeignKey(
        'references.Series',
        on_delete=models.PROTECT,
        verbose_name="Серия",
        blank=True,
        null=True)
    publishing_book = models.ForeignKey(
        'references.Publishing',
        on_delete=models.PROTECT,
        verbose_name="Издательство",
        blank=True,
        null=True)
    year_publishing = models.PositiveSmallIntegerField(
        verbose_name="Год издания",
        blank=True,
        null=True)
    number_of_pages = models.PositiveSmallIntegerField(
        verbose_name="Количество страниц",
        blank=True,
        null=True)
    binding = models.CharField(
        verbose_name="Тип обложки",
        max_length=30,
        blank=True,
        null=True)
    format_book = models.CharField(
        verbose_name="Формат книги",
        max_length=30,
        blank=True,
        null=True)
    isbn = models.CharField(
        verbose_name="ISBN",
        max_length=50,
        blank=True,
        null=True)
    weight = models.PositiveIntegerField(
        verbose_name="Вес книги",
        blank=True,
        null=True)
    age_restrictions = models.PositiveSmallIntegerField(
        verbose_name="Возрастные ограничения",
        blank=True,
        null=True)
    availability = models.BooleanField(
        verbose_name="Наличие товара",
        default=True)
    quantity = models.IntegerField(
        verbose_name="Количество",
        blank=True,
        default=0)                
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



