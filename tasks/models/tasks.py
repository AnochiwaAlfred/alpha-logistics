from django.db import models
from core.core import CoreBaseModel

# Create your models here.

TASKS_DISPLAY = ['id', 'cargo_type']
class Task(CoreBaseModel):
    order_id = models.ManyToManyField('orders.Order', related_name='orders')
    cargo_type = models.ForeignKey('cargo_types.CargoType', on_delete=models.CASCADE, related_name='cargo_type', null=True)
    
    def __str__(self):
        return f"Task {self.id}"
        
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'