from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, RedirectView
from order.models import Cart, CartItem
from product.models import Product
from order import utils
# Create your views here.

class AddCartView(DetailView):
    model = Cart
    template_name = 'add_cart.html'
    
    def get_object(self, *args, **kwargs):
        product_id = self.request.GET.get('product')
        if not product_id:
            current_cart_pk = self.request.session.get('current_cart_pk')
            if current_cart_pk:
                current_cart = Cart.objects.filter(pk=current_cart_pk).first()
                return current_cart or []
            return []    
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
                defaults={'quantity':1,}
            )
            if not created:
                product_item.quantity += 1
                product_item.save()
        return current_cart

class EditCart(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        current_cart_pk = self.request.session.get('current_cart_pk')
        if not current_cart_pk:
            reverse('cart:add-to-cart')
        cart_items = self.request.GET
        utils.update_items_in_cart(cart_items, current_cart_pk)
        return reverse('cart:add-to-cart')

 
    
