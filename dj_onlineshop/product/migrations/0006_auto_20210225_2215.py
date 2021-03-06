# Generated by Django 3.1.5 on 2021-02-25 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20210220_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(null=True, upload_to='uploads/', verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(blank=True, default=0, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, verbose_name='Количество'),
        ),
        migrations.DeleteModel(
            name='ProductsImage',
        ),
    ]
