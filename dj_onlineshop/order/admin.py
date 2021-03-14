from django.contrib import admin
from order import models

class CartAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'accepted',
        'total_sum',
    ]
    
    class Meta:
        model = models.Cart      

class CartItemAdmin(admin.ModelAdmin):
    list_display = [
        'cart',
        'product',
        'quantity',
        'price_sum']
    
    class Meta:
        model = models.CartItem

  


admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.CartItem)

