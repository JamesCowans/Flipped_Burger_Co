from django import forms

OPTION_QUANTITY_CHOICES  = [(i, str(i)) for i in range(1,21)]

class BasketAddOptionForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=OPTION_QUANTITY_CHOICES, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


