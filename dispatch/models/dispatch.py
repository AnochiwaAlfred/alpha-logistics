from django.db import models
from core.core import CoreBaseModel

# Create your models here.
DISPATCH_DISPLAY = ['id', 'task_id']

class Dispatch(CoreBaseModel):
    task_id = models.ForeignKey('tasks.Task', on_delete=models.CASCADE, related_name='task', null=True)
    
    def __str__(self):
        return self.task_id
    
        
    class Meta:
        verbose_name = 'Dispatch'
        verbose_name_plural = 'Dispatch'