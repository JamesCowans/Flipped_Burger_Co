from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from restaurant.models import Option
from .basket import Basket
from basket.forms import BasketAddOptionForm



# Create your views here.

@require_POST
def basket_add(request, option_id):
    basket = Basket(request)
    option = get_object_or_404(Option, id=option_id)
    form = BasketAddOptionForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        basket.add(option=option, quantity = cd['quantity'], override_quantity = cd['override'])
    return redirect('basket:basket_detail')



@require_POST
def basket_remove(request, option_id):
    basket = Basket(request)
    option = get_object_or_404(Option, id=option_id)
    basket.remove(option)
    return redirect('basket:basket_detail')





def basket_detail(request):
    basket = Basket(request)
    for item in basket:
        item['update_quantity_form'] = BasketAddOptionForm(initial={
                            'quantity': item['quantity'],
                            'override': True})
    return render(request, 'basket/detail.html', {'basket': basket})

