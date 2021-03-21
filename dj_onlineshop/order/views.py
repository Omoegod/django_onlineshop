from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, RedirectView, View, UpdateView, ListView
from order.models import Cart, CartItem, Order
from product.models import Product
from profiles.models import Profile
from order import utils, forms
# Create your views here.


def get_cart(request):
    current_cart_pk = request.session.get('current_cart_pk')
    current_user = request.user
    if current_user.is_anonymous:
        current_user = None
    current_cart, created = Cart.objects.get_or_create( 
        pk = current_cart_pk,
        defaults={'user':current_user}
    )
    return current_cart, created

class AddProductCart(UpdateView):
    model = CartItem
    template_name = 'add.html'
    success_url = '/books/'
    fields = ()

    def get_object(self, *args, **kwargs):
        product_id = self.request.GET.get('product')
        product = Product.objects.get(pk=product_id)
        current_cart, created = get_cart(self.request)
        if created:
            self.request.session['current_cart_pk'] = current_cart.pk
        product_item, created = CartItem.objects.get_or_create(
            cart = current_cart,
            product = product,
            defaults={'quantity':1,}
            )
        return product_item

class CartDetail(DetailView):
    model = Cart
    template_name = 'cart.html'
    def get_object(self, *args, **kwargs):
        current_cart = get_cart(self.request)
        current_cart, created = get_cart(self.request)
        if created:
            self.request.session['current_cart_pk'] = current_cart.pk
        return current_cart

class EditCart(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        current_cart_pk, cart_items = utils.harvest_data(self) 
        if not current_cart_pk:
            return reverse('cart:cart-detail')
        action = utils.update_items_in_cart(cart_items, current_cart_pk)
        if action == 'checkout':
            url = reverse('cart:checkout')
        else:
            url = reverse('cart:cart-detail')
        return url

class CheckOutView(UpdateView):
    model = Order
    template_name = 'checkout.html'
    fields = ('customer_name', 'address', 'phone_number')
    success_url = reverse_lazy('home') 

    def get_object(self, *args, **kwargs):
        order_pk = self.request.GET.get('order')
        current_cart_pk = self.request.session['current_cart_pk']
        if not order_pk:
            current_cart = Cart.objects.filter(pk = current_cart_pk).first()
            user_name = self.request.user
            if user_name.is_anonymous:
                user_name = None
            order, created = Order.objects.get_or_create(
                cart = current_cart,
                username = user_name,
                defaults = {   
                'customer_name': 'Введите ваше имя',
                'address' : 'Введите ваш адрес',
                'phone_number' : '+375',
                'total_sum_order' : current_cart.total_sum
             })
            return order        
        else: 
            order = Order.objects.get(pk = order_pk)
            return order          
    
    def get_success_url(self):
        url = super().get_success_url()
        del(self.request.session['current_cart_pk'])
        return url

class OrderListInProfile(ListView):
    model = Order
    template_name = 'profiles/account_detail_order.html'
    
    def get(self, request):
        user_name = self.request.user
        category = Order.objects.filter(username=user_name)
        context = {
            'category':category,
        }   
        return render(request, self.template_name, context)


class OrderDetail(DetailView):
    model = Order
    template_name = 'profiles/order_detail.html'

class StatusOrderUpdate(UpdateView):
    model = Order
    form_class = forms.OrderUpdate
    template_name = 'profiles/order_update.html'
    success_url = reverse_lazy('cart:order-list')

