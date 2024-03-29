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

class TestModels(TestCase):
    def setUp(self):
        First_name.objects.create(first_name='testfirst'),
        Last_name.objects.create(last_name='testlast'),
        Email.onjects.create(email='test@email.com'),
        Address.objects.create(address='testAddress'),
        Town.objects.create(town='testTowm'),
        Post_code.objects.create('testPostcode'),
        Comments.objects.create('testComment')


    def customer_order(self):
        # customer_order = Order.objects.create(
        first_name = First_name.objects.create(name="lion")
            # first_name='Steve',
            # last_name='Cowans',
            # email='Jamescowans@hotmail.com',
            # address='here',
            # town='there',
            # post_code = 'NE32FP',
            # comment = 'test'
        # )


        # self.assertEquals(str(first_name), 'James')
        self.assertEqual(first_name.name(), 'lion' )
    # self.assertTrue(isinstance(customer_order, Order))
