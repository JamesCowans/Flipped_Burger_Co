from decimal import Decimal
from django.conf import settings
from restaurant.models import Option


class Basket():
    
    def __init__(self, request):
        
        self.session = request.session
        basket = self.session.get('basket_session')
        
        if 'basket_session' not in request.session:
            
            basket = self.session['basket_session'] = {}
            
        self.basket = basket
        
        
    def add(self, option):
        
        option_id = str(option.id)
        
        if option_id in self.basket:
            
            self.basket[option_id]['qty'] = option_qty
            
        else:
            
            self.basket[option_id] = {'price': str(option.price), 'qty' : option_qty}
            
        self.session.modified = True
        

        