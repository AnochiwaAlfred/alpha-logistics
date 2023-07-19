from django.db import models
from core.core import CoreBaseModel

# Create your models here.
SUB_CATEGORIES_DISPLAY = ['name', 'is_active', ]

class SubCategory(CoreBaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Sub Category'
        verbose_name_plural = 'Sub Categories'