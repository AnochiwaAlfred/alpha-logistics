
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from django.urls import path, include, re_path
# from apis.api import api


VERSION = 'v1'

urlpatterns = [
    path('admin/', admin.site.urls),
    # path(f"api/{VERSION}/", api.urls ),
    
    re_path(r'^media/(?P<path>.*)$', serve,  {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

]