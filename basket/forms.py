from django import forms

OPTION_QUANTITY_SELECTIONS  = [(i, str(i)) for i in range(1,21)]

class BasketAddOptionForm(forms.Form):
    quantity = forms.TypeChoiceField(selections=OPTION_QUANTITY_SELECTIONS, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


