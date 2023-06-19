from ninja import Router, Form
from django.shortcuts import get_object_or_404
from alpha_logistics.schemas.products import *
from products.models.products import *
from authuser.models import User
from categories.models import Category
from typing import List

router = Router(tags=['Products'])

@router.post('/add', response=ProductOutSchema)
def add_product(request, user_id, category_id, data:ProductInSchema=Form(...)):
    user = get_object_or_404(User, id=user_id)
    category = get_object_or_404(Category, id=category_id)
    product = Product.objects.create(**data.dict())
    product.category_id = category
    product.user_id = user
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
def update_product(request, id, data:ProductInSchema, user_id=None, category_id=None):
    product = get_object_or_404(Product, id=id)
    for attr, value in data.dict().items():
        setattr(product, attr, value)
    if user_id!=None:
        user = get_object_or_404(User, id=user_id)
        product.user_id=user
    if category_id!=None:
        category = get_object_or_404(Category, id=category_id)
        product.category_id=category
    product.save()
    return product

@router.delete('/delete/{id}')
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return f"Product {product.name} deleted successfully"
