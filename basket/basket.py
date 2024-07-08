from decimal import Decimal
from django.conf import settings
from restaurant.models import Option


class Basket():
    
    def __init__(self, request):
        
        self.session = request.session
        basket = self.session.get('session_key')
        
        if 'session_key' not in request.session:
            
            basket = self.session['session_key'] = {}
            
        self.basket = basket
        
        
    def add(self, option):
        
        option_id = str(option.id)
        
        if option_id in self.basket:
            
            self.basket[option_id]['qty'] = option_qty
            
        else:
            
            self.basket[option_id] = {'price': str(option.price), 'qty' : option_qty}
            
        self.session.modified = True
        

        