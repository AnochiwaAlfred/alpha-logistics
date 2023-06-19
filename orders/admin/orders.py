from django.contrib import admin
from orders.models.orders import *

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ORDER_DISPLAY