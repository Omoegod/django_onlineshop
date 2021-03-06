# Generated by Django 3.1.5 on 2021-02-20 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210217_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='age_restrictions',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Number of page'),
        ),
        migrations.AddField(
            model_name='product',
            name='availability',
            field=models.BooleanField(default=True, verbose_name='Наличие товара'),
        ),
        migrations.AddField(
            model_name='product',
            name='binding',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Тип обложки'),
        ),
        migrations.AddField(
            model_name='product',
            name='format_book',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Формат книги'),
        ),
        migrations.AddField(
            model_name='product',
            name='isbn',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Number of page'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0, verbose_name='Количество'),
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Number of page'),
        ),
        migrations.AlterField(
            model_name='productsimage',
            name='image',
            field=models.ImageField(upload_to='image/'),
        ),
    ]
