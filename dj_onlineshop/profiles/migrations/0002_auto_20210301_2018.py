# Generated by Django 3.1.5 on 2021-03-01 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профиля'},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='password2',
        ),
    ]
