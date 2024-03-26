from django import forms
from .models import Order


class OrderPlacementForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'town', 'post_code', 'comments']