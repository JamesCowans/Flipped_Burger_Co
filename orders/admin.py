from django.contrib import admin

# Register your models here.

from . models import Order, OrderItem

class OrderItemInQueue(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['option']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'post_code', 'town', 'created', 'updated' ]
    list_filter = ['created', 'updated']
    inlines = [OrderItemInQueue]