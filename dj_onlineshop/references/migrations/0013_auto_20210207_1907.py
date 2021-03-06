# Generated by Django 3.1.5 on 2021-02-07 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0012_auto_20210206_2347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='descriptions',
            new_name='descriptions_author',
        ),
        migrations.AddField(
            model_name='genre',
            name='descriptions_genre',
            field=models.TextField(blank=True, null=True, verbose_name='Descriptions Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='descriptions_book',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Descriptions book'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name_genre',
            field=models.CharField(max_length=50, verbose_name='Name genre'),
        ),
        migrations.AlterField(
            model_name='series',
            name='name_series',
            field=models.CharField(max_length=50, verbose_name='Name series'),
        ),
    ]
