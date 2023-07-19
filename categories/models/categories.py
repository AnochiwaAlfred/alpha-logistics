from django.db import models
from core.core import *

# Create your models here.

CATEGORIES_DISPLAY = ['name']

class Category(CoreBaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'