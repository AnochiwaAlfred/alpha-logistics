from django.db import models
from core.core import *

# Create your models here.

CARGO_TYPE_DISPLAY = ['name']

class CargoType(CoreBaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Cargo Type'
        verbose_name_plural = 'Cargo Types'