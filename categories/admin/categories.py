from django.contrib import admin
from categories.models import *

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = CATEGORIES_DISPLAY
    list_filter = ['is_active']
    list_display_links = ['name']