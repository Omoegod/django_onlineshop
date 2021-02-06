# Generated by Django 3.1.5 on 2021-02-06 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('happyworld', '0007_auto_20210204_2356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_book', models.CharField(max_length=100, verbose_name='Name book')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Created date')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Updated date')),
                ('author_book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='happyworld.author', verbose_name='Author')),
            ],
        ),
    ]
