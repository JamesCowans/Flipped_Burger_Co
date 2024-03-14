from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import OrderItem, Order
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
        form = OrderPlacementForm()
    return render(request, 'orders/order/place.html', {'basket': basket, 'form': form})

def order_placed(order_id):
    order = Order.objects.get(id=order_id)
    


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/order/detail.html', {'order' : order})