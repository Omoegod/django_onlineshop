# Generated by Django 3.1.5 on 2021-03-21 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20210313_1239'),
        ('order', '0010_auto_20210320_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='username',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='profiles.profile', verbose_name='User'),
        ),
    ]
