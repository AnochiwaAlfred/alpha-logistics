from django.db import models
from core.core import *
# Create your models here.

ORDER_DISPLAY = ['id', 'product_id', 'quantity', 'created']

class Order(CoreBaseModel):
    client_id = models.ForeignKey('authuser.Client', on_delete=models.CASCADE, related_name='order_client', null=True)
    product_id = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='product', null=True)
    quantity = models.IntegerField()
    
    def __str__(self):
        return f"Order {self.id}"
        
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'