from ninja import Router, Form
from django.shortcuts import get_object_or_404
from alpha_logistics.schemas.categories import *
from categories.models.categories import *
from typing import List

router = Router(tags=['Categories'])


@router.post('/add', response=CategoryOutSchema)
def add_category(request, data:CategoryInSchema=Form(...)):
    category = Category.objects.create(**data.dict())
    return category

@router.get('/category/{id}', response=CategoryOutSchema)
def get_category(request, id):
    category = get_object_or_404(Category, id=id)
    return category

@router.get('/list', response=List[CategoryOutSchema])
def list_categories(request):
    d_list = Category.objects.all()
    return d_list

@router.put('/change/{id}', response=CategoryOutSchema)
def update_category(request, id, data:CategoryInSchema):
    category = Category.objects.filter(id=id)[0]
    for attr, value in data.dict().items():
        setattr(category, attr, value)
    category.save()
    return category

@router.delete('/delete/{id}')
def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return f"Category {category.name} deleted successfully"