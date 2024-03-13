from django.shortcuts import render
from .models import OrderItem
from .forms import OrderPlacementForm
from basket.basket import Basket


# Create your views here.

def order_place(request):
    basket = Basket(request)
    if request.method == 'POST':
        form = OrderPlacementForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in basket:
                OrderItem.objects.create(order=order, option = item['option'], price=item['price'], quantity=item['quantity'])

                basket.empty_basket()
                return render(request,'orders/order/placed.html',{'order': order})
    else:
        form =OrderPlacementForm()
    return render(request, 'orders/order/place.html', {'basket': basket, 'form': form})