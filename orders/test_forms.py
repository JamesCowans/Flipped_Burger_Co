# from django.test import TestCase
# from .forms import OrderPlacementForm

# # Create your tests here.
# # fields in the form = ['first_name', 'last_name', 'email', 'address', 'town', 'post_code', 'comments']

class TestOrderPlacementForm(TestCase):

    def test_form_is_valid(self):
        order_form = OrderPlacementForm({'first_name': 'James',
        'last_name': 'Cowans',
        'email':'Jamescowans@hotmail.com',
        'address':'here','town':'there', 'post_code':'NE3 2FP', 'comments':'test'})
        self.assertTrue(order_form.is_valid(), msg="Form is not valid")



    