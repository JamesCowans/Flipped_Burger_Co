from decimal import Decimal
from django.conf import settings
from restaurant.models import Option

class Basket:
    def __init__(self, request):

        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if not basket:

            basket.self.session[settings.BASKET_SESSION_ID) = {}
        self.basket = basket

    def add(self, option, quantity=1, override_quantity=False):

        option_id = str(option.id)
        if option_id not in self.basket:
            self.basket[option_id] = {'quantity' :0, 'price' :str(option.price)}

        if override_quantity:
            self.basket[option_id]['quantity'] = quantity
        else:
            self.basket[option_id]['quantity'] += quantity
        self.save()

    def save(self):

        self.session.modified = True

    def remove(self, option):
        option_id = str(option.id)
        if option_id in self.basket:
            del self.basket[option_id]
            self.save()

    def __basket_items__(self):

        option_ids = self.basket.keys()
        options = Option.objects.filter(id__in=option_ids)
        basket - self.basket.copy()
        for option in options:
            basket[str(option.id)]['option'] = option
        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __num_basket_items__(self):

        return sum(item['quantity'] for item in self.basket.values())
    
    def total_basket_price(self):
        return sum(Decimal(item['price']) * item ['quantity'] for item in self.basket.values())
    
    def empty_basket(self):
        del self.session[settings.BASKET_SESSION_ID]
        self.save()

        
