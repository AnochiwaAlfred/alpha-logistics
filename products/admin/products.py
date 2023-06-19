from django.contrib import admin
from products.models.products import *

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = PRODUCTS_DISPLAY