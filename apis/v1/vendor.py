from ninja import Router, Form
from django.shortcuts import get_object_or_404
from alpha_logistics.schemas.auth import *
from authuser.models.user import *
from typing import List

router = Router(tags=['Vendors'])


@router.post('/add', response=VendorOutSchema)
def add_vendor(request, data:VendorInSchema=Form(...)):
    vendor = Vendor.objects.create(**data.dict())
    return vendor

@router.get('/vendor/{id}', response=VendorOutSchema)
def get_vendor(request, id):
    vendor = get_object_or_404(Vendor, id=id)
    return vendor

@router.get('/list', response=List[VendorOutSchema])
def list_vendors(request):
    d_list = Vendor.objects.all()
    return d_list

@router.put('/change/{id}', response=VendorOutSchema)
def update_vendor(request, id, data:VendorInSchema):
    vendor = Vendor.objects.filter(id=id)[0]
    for attr, value in data.dict().items():
        setattr(vendor, attr, value)
    vendor.save()
    return vendor

@router.delete('/delete/{id}')
def delete_vendor(request, id):
    vendor = get_object_or_404(Vendor, id=id)
    vendor.delete()
    return f"Vendor {vendor.name} deleted successfully"