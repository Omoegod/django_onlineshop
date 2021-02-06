# Generated by Django 3.1.5 on 2021-02-06 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happyworld', '0010_auto_20210206_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='number_of_pages',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Number of page'),
        ),
        migrations.AlterField(
            model_name='book',
            name='descriptions_book',
            field=models.TextField(blank=True, default='-', null=True, verbose_name='Descriptions book'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year_publishing',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Year publishing'),
        ),
    ]
