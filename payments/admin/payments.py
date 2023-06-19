from django.contrib import admin
from payments.models.payments import *

# Register your models here.
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = PAYMENTS_DISPLAY