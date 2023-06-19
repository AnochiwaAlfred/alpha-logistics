from django.contrib import admin
from tasks.models.tasks import *

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = TASKS_DISPLAY