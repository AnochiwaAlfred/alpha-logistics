from django.contrib import admin
from django.http.response import HttpResponse
from authuser.models import *
import uuid
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# @admin.register(Agent)
# @admin.register(Driver)
# @admin.register(Vendor)
@admin.register(CustomUser)
class UserAdmin(BaseUserAdmin):
    search_fields = ['email__startswith']
    list_display = ['email', 'username', 'is_staff', 'is_superuser']
    list_filter = ['is_superuser']
    list_display_links = ['email', 'username']
    filter_horizontal = []
    ordering = ['id']
    fieldsets = [
        (None, {'fields': ['email', 'password']}),
        ('Personal Info', {'fields':[]}),
        ('Permissions', {'fields':['is_staff', 'is_superuser']}),
    ]
    
    def response_add(self, request, obj, post_url_continue=None) -> HttpResponse:
        coded = str(uuid.uuid4()).replace("-", "")[:4]
        code = f"bom{coded}"
        obj.code = code
        obj.save()
        return super().response_add(request, obj, post_url_continue)
        
    


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = [
            'email',
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit=False):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    
    class Meta:
        model = CustomUser
        fields = '__all__'
        exclude = [
            'last_login', 
            'created_at', 
            'key', 
            'message', 
            'encoded',
            'encrypt_date',
            'rsa_duration'
        ]


@admin.register(Agent)
class AgentAdmin(UserAdmin):
    search_fields = ['email__startswith']
    list_display = ['email', 'username', 'is_staff', 'first_name', 'last_name']
    list_filter = ['is_superuser']
    list_display_links = ['email', 'username']
    filter_horizontal = []
    ordering = ['id']
    fieldsets = [
        (None, {'fields': ['email', 'password']}),
        ('Personal Info', {'fields':['first_name', 'last_name', 'phone', 'address']}),
        ('Permissions', {'fields':['is_staff', 'is_superuser']}),
    ]
    
    def response_add(self, request, obj, post_url_continue=None) -> HttpResponse:
        coded = str(uuid.uuid4()).replace("-", "")[:4]
        code = f"bom{coded}"
        obj.code = code
        obj.save()
        return super().response_add(request, obj, post_url_continue)
        
    

@admin.register(Driver)
class DriverAdmin(UserAdmin):
    search_fields = ['email__startswith']
    list_display = ['email', 'username', 'is_staff', 'first_name', 'last_name']
    list_filter = ['is_superuser']
    list_display_links = ['email', 'username']
    filter_horizontal = []
    ordering = ['id']
    fieldsets = [
        (None, {'fields': ['email', 'password']}),
        ('Personal Info', {'fields':['first_name', 'last_name', 'phone', 'gender', 'address']}),
        ('Permissions', {'fields':['is_staff', 'is_superuser']}),
    ]
    
    def response_add(self, request, obj, post_url_continue=None) -> HttpResponse:
        coded = str(uuid.uuid4()).replace("-", "")[:4]
        code = f"bom{coded}"
        obj.code = code
        obj.save()
        return super().response_add(request, obj, post_url_continue)
        
    
@admin.register(Vendor)
class VendorAdmin(UserAdmin):
    search_fields = ['email__startswith']
    list_display = ['email', 'username', 'is_staff', 'first_name', 'last_name']
    list_filter = ['is_superuser']
    list_display_links = ['email', 'username']
    filter_horizontal = []
    ordering = ['id']
    fieldsets = [
        (None, {'fields': ['email', 'password']}),
        ('Personal Info', {'fields':['first_name', 'last_name', 'phone', 'gender', 'address', 'country']}),
        ('Permissions', {'fields':['is_staff', 'is_superuser']}),
    ]
    
    def response_add(self, request, obj, post_url_continue=None) -> HttpResponse:
        coded = str(uuid.uuid4()).replace("-", "")[:4]
        code = f"bom{coded}"
        obj.code = code
        obj.save()
        return super().response_add(request, obj, post_url_continue)