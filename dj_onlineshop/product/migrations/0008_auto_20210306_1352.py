# Generated by Django 3.1.5 on 2021-03-06 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20210228_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, max_length=200, upload_to='uploads/', verbose_name='Фотография'),
        ),
    ]
