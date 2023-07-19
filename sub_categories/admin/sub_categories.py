from django.contrib import admin
from sub_categories.models import *

# Register your models here.

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = SUB_CATEGORIES_DISPLAY
    list_filter = ['is_active']
    list_display_links = ['name']
    