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
    total_sum_cart = models.DecimalField(
        verbose_name='Сумма',
        default=0,
        max_digits=10,
        decimal_places=2,    )

    @property
    def total_sum(self):
        all_item = self.products_item.all()
        self.total_sum_cart = 0
        for product in all_item:
            self.total_sum_cart += product.total_price
            super().save()
        return self.total_sum_cart
        


    def __str__(self):
        return f'{self.pk}'



class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        verbose_name='Корзина',
        on_delete=models.CASCADE,
        related_name='products_item',
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
    total_sum_item = models.DecimalField(
        verbose_name='Сумма',
        default=0,
        max_digits=10,
        decimal_places=2,
    )
    @property
    def total_price(self):
        self.total_sum_item = self.quantity * self.product.price
        super().save()
        return self.total_sum_item


    def __str__(self):
        return f'{self.pk}'


class Order(models.Model):
    cart = models.ForeignKey(
        Cart,
        verbose_name='Cart',
        on_delete=models.PROTECT)
    address = models.TextField('Address')
    def __str__(self):
        return f'order # {self.pk}'
