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
    

class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        verbose_name='Корзина',
        on_delete=models.CASCADE,
        related_name='cart_item',
    )
    product = models.ForeignKey(
        Product,
        verbose_name='Товар',
        on_delete=models.CASCADE,       
    )
    quantity = models.PositiveIntegerField(
        default = 1,
    )    
    price_sum = models.DecimalField(
        verbose_name='Сумма товаров',
        default=0,
        max_digits=10,
        decimal_places=2,
    )
    def save(self, *args, **kwargs):
        self.price_sum = self.quantity * self.product.price
        super().save(*args, **kwargs)
    def __str__(self):
        return f'CartItem # {self.pk} {self.product.name_book} quantity {self.quantity}'
    
        
class Order(models.Model):
    cart = models.OneToOneField(
        Cart,
        verbose_name='Cart', 
        on_delete=models.PROTECT)
    address = models.TextField('Address')    
    def __str__(self):
        return f'order # {self.pk}'
    