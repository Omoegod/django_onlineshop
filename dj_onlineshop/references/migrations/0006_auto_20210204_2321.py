# Generated by Django 3.1.5 on 2021-02-04 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0005_auto_20210131_2148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='name',
            new_name='name_author',
        ),
    ]