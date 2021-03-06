# Generated by Django 3.1.5 on 2021-03-19 16:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20210313_1656'),
        ('order', '0008_auto_20210315_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='customer_name',
            field=models.CharField(default='фио', max_length=30, verbose_name='ФИО'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.CharField(default='+', max_length=15, verbose_name='Телефон'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='total_sum_order',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Сумма'),
        ),
        migrations.AddField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=250, verbose_name='Address'),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('total_sum_item', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Сумма')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_item_order', to='order.order', verbose_name='Корзина')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Товар')),
            ],
        ),
    ]
