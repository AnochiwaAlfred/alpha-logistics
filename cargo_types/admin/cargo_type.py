from django.contrib import admin
from cargo_types.models import *

# Register your models here.

@admin.register(CargoType)
class CargoTypeAdmin(admin.ModelAdmin):
    list_display = CARGO_TYPE_DISPLAY