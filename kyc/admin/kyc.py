from django.contrib import admin
from kyc.models.kyc import *

# Register your models here.

@admin.register(KYC)
class AdminKYC(admin.ModelAdmin):
    list_display = KYC_DISPLAY