from django.db import models
from core.core import *
from django_countries import countries

# Create your models here.
KYC_DISPLAY = ['user_id', 'first_name', 'last_name', 'country', 'state', 'city']
COUNTRY_LIST =  tuple([(code, name) for code, name in countries])
class KYC(CoreBaseModel):
    user_id = models.ForeignKey('authuser.User', on_delete=models.CASCADE, related_name='KYC_user', null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    country = models.CharField(max_length=200, choices=COUNTRY_LIST)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        
    class Meta:
        verbose_name = 'KYC'
        verbose_name_plural = 'KYC'
