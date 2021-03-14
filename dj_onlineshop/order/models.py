from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product

User = get_user_model()

class Cart(models.Model):
    session = models.CharField(
        verbose_name='Корзина пользователя',
        max_length=500,
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        User,
        verbose_name='Покупатель',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    accepted = models.BooleanField(
        verbose_name='Принято к заказу',
        default=False,
    )
    total_sum = models.DecimalField(
        verbose_name='Сумма',
        default=0,
        max_digits=10,
        decimal_places=2,
    )

    def total_sum(self):
        all_item = self.products.all()
        total = 0
        for product in all_item:
            total += product.total_price()
        return total

    def __str__(self):
        return self.pk



class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        verbose_name='Корзина',
        on_delete=models.CASCADE,
        related_name='products',
    )
    product = models.ForeignKey(
        Product,
        verbose_name='Товар',
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField(
        'Количество',
        default = 1,
    )
    price_sum = models.DecimalField(
        verbose_name='Сумма',
        default=0,
        max_digits=10,
        decimal_places=2,
    )
    
    def total_price(self):
        self.price_sum = self.quantity * self.product.price
        super().save()
        return self.price_sum


    def __str__(self):
        return f'CartItem # {self.pk} {self.product.name_book} quantity {self.quantity} sum {self.price_sum}'


class Order(models.Model):
    cart = models.ForeignKey(
        Cart,
        verbose_name='Cart',
        on_delete=models.PROTECT)
    address = models.TextField('Address')
    def __str__(self):
        return f'order # {self.pk}'
