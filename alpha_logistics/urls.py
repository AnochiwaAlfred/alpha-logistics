
from django.contrib import admin
from django.urls import path
from apis.api import api
VERSION = 'v1'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f"api/{VERSION}/", api.urls )

]