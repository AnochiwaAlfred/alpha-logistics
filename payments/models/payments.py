from django.db import models
from core.core import CoreBaseModel

# Create your models here.
PAYMENTS_DISPLAY = ['id', 'order_id']


class Payment(CoreBaseModel):
    order_id = models.ForeignKey('orders.Order', on_delete=models.CASCADE, related_name='payment_order', null=True)
    
    def __str__(self):
        return f"Payment {self.id}"
    
    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'