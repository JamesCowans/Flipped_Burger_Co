
from django.contrib import admin
from django.urls import reverse
from . models import Order, OrderItem

# Register your models here.



class OrderItemInQueue(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['option']


def order_detail(obj):
    url = reverse('orders:admin_order_detail', args=[obj.id])
    return mark_safe(f'<a href="{url}">View</a>')
                  

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'post_code', 'town', 'created', 'updated' ]
    list_filter = ['created', 'updated']
    inlines = [OrderItemInQueue]