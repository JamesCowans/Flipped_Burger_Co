from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('place/', views.order_place, name ='order_place'),
    path('admin/order/<int:order_id>/', views.admin_order_detail, name='admin_order_detail'),

]