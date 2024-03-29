from django.test import TestCase
from .models import Order

# Create your tests here.

# Class Order(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length =50)
#     email = models.EmailField()
#     address = models.CharField(max_length=250)
#     town =  models.CharField(max_length=50)
#     post_code = models.CharField(max_length=10)   
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     comments = models.TextField(blank=True)

class TestOrderModel(TestCase):
    def test_model_order(self):
        test_order = Order(
        first_name = First_name.objects.create(first_name='testfirst'),
        last_name = Last_name.objects.create(last_name='testlast'),
        email = Email.onjects.create(email='test@email.com'),
        address = Address.objects.create(address='testAddress'),
        town = Town.objects.create(town='testTowm'),
        post_code = Post_code.objects.create('testPostcode'),
        comments = Comments.objects.create('testComment')

        customer_order = CustomerOrder.objects.create(
            first_name='James',
            last_name='Cowans',
            email='Jamescowans@hotmail.com',
            address='here',
            town='there',
            post_code = 'NE32FP',
            comment = 'test'
        )


        # self.assertEquals(str(customer_order), 'James')
        self.assertTrue(isinstance(customer_order, CustomerOrder))
