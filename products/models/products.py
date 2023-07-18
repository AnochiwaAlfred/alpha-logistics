from django.db import models
from core.core import *

# Create your models here.
PRODUCTS_DISPLAY = ['name', 'category_id', 'user_id', 'weight', 'created']
class Product(CoreBaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    user_id = models.ForeignKey('authuser.Vendor', on_delete=models.CASCADE, related_name='product_user', null=True)
    category_id = models.ForeignKey('categories.Category', on_delete=models.CASCADE, related_name='category', null=True)
    weight = models.IntegerField()
    
    # recepient_fullname = models.CharField(max_length=255)
    # recepient_email = models.CharField(max_length=255)
    # recepient_phone = models.CharField(max_length=255)
    # recepient_address = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'