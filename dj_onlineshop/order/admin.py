from django.contrib import admin
from order import models

class CartAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'accepted',
        'total_sum_cart',]
    
    class Meta:
        model = models.Cart      

class CartItemAdmin(admin.ModelAdmin):
    list_display = [
        'cart',
        'product',
        'quantity',
        'total_sum_item']
    
    class Meta:
        model = models.CartItem


class OrderAdmin(admin.ModelAdmin): 
    list_display = [
        'cart',
        'customer_name',
        'address',
        'phone_number',
        'total_sum_order',
        'actions',
        'created',
        'updated']
    # inlines = [OrderItemAdmin]

admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.CartItem, CartItemAdmin)
admin.site.register(models.Order, OrderAdmin)


