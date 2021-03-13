from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, DetailView
from order.models import Cart, CartItem
from product.models import Product

# Create your views here.

class AddCartView(DetailView):
    model = Cart
    template_name = 'add_cart.html'
    def get_object(self, *args, **kwargs):
        product_id = self.request.GET.get('product')
        if not product_id:
            pass
        else:
            current_cart_pk = self.request.session.get('current_cart_pk')
            current_user = self.request.user
            if current_user.is_anonymous:
                current_user = None
            current_cart, created = Cart.objects.get_or_create( 
                pk = current_cart_pk,
                defaults={'user':current_user}
            )
            if created:
                self.request.session['current_cart_pk'] = current_cart.pk
                self.request.session['current_cart_pk']
            product = Product.objects.get(pk=product_id)    
            product_item, created = CartItem.objects.get_or_create(
                cart = current_cart,
                product = product,
                defaults={
                    'quantity':1,
                    'price_sum': Product.price }
            )
            if not created:
                product_item.quantity += 1
                product_item.save()
        return current_cart