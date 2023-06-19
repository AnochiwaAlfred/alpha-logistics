from django.contrib import admin
from dispatch.models.dispatch import *

# Register your models here.
@admin.register(Dispatch)
class DispatchAdmin(admin.ModelAdmin):
    list_display = DISPATCH_DISPLAY