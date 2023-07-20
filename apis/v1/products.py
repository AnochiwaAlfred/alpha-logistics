from ninja import Router, Form
from django.shortcuts import get_object_or_404
from alpha_logistics.schemas.products import *
from products.models.products import *
from authuser.models import Vendor
from sub_categories.models import SubCategory
from typing import List

router = Router(tags=['Products'])

@router.post('/add', response=ProductOutSchema)
def add_product(request, data:ProductInSchema=Form(...)):
    vendor_id = get_object_or_404(Vendor, id=int(data.dict().get('vendor_id')))
    sub_category_id = get_object_or_404(SubCategory, id=uuid.UUID(data.dict().get('sub_category_id')))
    data_p = data.dict()
    data_p.pop('vendor_id')
    data_p.pop('sub_category_id')
    product = Product.objects.create(**data_p)
    product.sub_category_id=sub_category_id
    product.vendor_id=vendor_id
    product.save()
    return product

@router.get('/product/{id}', response=ProductOutSchema)
def get_product(request, id):
    product = get_object_or_404(Product, id=id)
    return product


@router.get('/list', response=List[ProductOutSchema])
def list_product(request):
    products = Product.objects.all()
    return products


@router.put('/change/{id}', response=ProductOutSchema)
def update_product(request, id, data:ProductInSchema):
    vendor_id = get_object_or_404(Vendor, id=int(data.dict().get('vendor_id')))
    sub_category_id = get_object_or_404(SubCategory, id=uuid.UUID(data.dict().get('sub_category_id')))
    data_p = data.dict()
    data_p.pop('vendor_id')
    data_p.pop('sub_category_id')
    product = Product.objects.filter(id=id)[0]
    for attr, value in data_p.items():
        setattr(product, attr, value)
    product.vendor_id=vendor_id
    product.sub_category_id=sub_category_id
    product.save()
    return product

@router.delete('/delete/{id}')
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return f"Product {product.name} deleted successfully"
