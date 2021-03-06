# Generated by Django 3.1.5 on 2021-02-28 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20210225_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='isbn',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, default='empty', upload_to='uploads/', verbose_name='Фотография'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, verbose_name='Цена'),
        ),
    ]
