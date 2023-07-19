from django.db import models
from core.core import CoreBaseModel

# Create your models here.

TASKS_DISPLAY = ['id', 'driver_id', 'created']
class Task(CoreBaseModel):
    order_id = models.ManyToManyField('orders.Order', related_name='orders')
    driver_id = models.ForeignKey('authuser.Driver', on_delete=models.CASCADE, related_name='driver_id', null=True)
    
    def __str__(self):
        return f"Task {self.id}"
        
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'