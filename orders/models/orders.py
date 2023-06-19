from django.db import models
from core.core import *
# Create your models here.

ORDER_DISPLAY = ['id', 'user_id', 'created']

class Order(CoreBaseModel):
    user_id = models.ForeignKey('authuser.User', on_delete=models.CASCADE, related_name='order_user', null=True)
    product_id = models.ManyToManyField('products.Product', related_name='products')
    
    def __str__(self):
        return f"Order {self.id}"
        
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'