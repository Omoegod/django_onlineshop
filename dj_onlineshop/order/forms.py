from django import forms
from order.models import Order

class OrderUpdate(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['actions']                       

