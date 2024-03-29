from django import forms
from .models import Order


class OrderPlacementForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'town', 'post_code', 'comments']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'town': forms.TextInput(attrs={'class': 'form-control'}),
            'post_code': forms.TextInput(attrs={'class': 'form-control'}),
            'comments': forms.Textarea(attrs={'class': 'form-control'}),
        }
