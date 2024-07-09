from django.urls import path
from . import views

app_name = 'basket'

urlpatterns = [
    path('', views.basket_detail, name='basket-detail'),
    path('add/<int:option_id>/', views.basket_add, name='basket-add'),
    path('remove/<int:option_id>/', views.basket_remove, name='basket-remove'),
    path('update/', views.basket_update, name='basket-update'),
]


