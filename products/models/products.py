from django.db import models
from core.core import *

# Create your models here.
PRODUCTS_DISPLAY = ['name', 'sub_category_id', 'vendor_id', 'price']
class Product(CoreBaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    vendor_id = models.ForeignKey('authuser.Vendor', on_delete=models.CASCADE, related_name='product_vendor', null=True)
    sub_category_id = models.ForeignKey('sub_categories.SubCategory', on_delete=models.CASCADE, related_name='sub_category', null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'