from ninja import Router, Form
from django.shortcuts import get_object_or_404
from alpha_logistics.schemas.sub_categories import *
from sub_categories.models.sub_categories import *
from categories.models.categories import *

from typing import List

router = Router(tags=['Sub Categories'])

@router.post('/add', response=SubCategoryOutSchema)
def add_sub_category(request, data:SubCategoryInSchema=Form(...)):
    category_id =uuid.UUID(data.dict().get('category_id'))
    category = get_object_or_404(Category, id=category_id)
    sub_category = SubCategory.objects.create(**data.dict())
    print(sub_category)
    sub_category.category = category
    sub_category.save()
    return sub_category

@router.get('/category/{id}', response=SubCategoryOutSchema)
def get_sub_category(request, id):
    sub_category = get_object_or_404(SubCategory, id=id)
    return sub_category

@router.get('/list', response=List[SubCategoryOutSchema])
def list_sub_category(request):
    d_list = SubCategory.objects.all()
    return d_list

@router.put('/change/{id}', response=SubCategoryOutSchema)
def update_sub_category(request, id, data:SubCategoryInSchema):
    category_id =uuid.UUID(data.dict().get('category_id'))
    category = get_object_or_404(Category, id=category_id)
    sub_category = SubCategory.objects.filter(id=id)[0]
    for attr, value in data.dict().items():
        setattr(sub_category, attr, value)
    sub_category.category = category
    sub_category.save()
    return sub_category

@router.delete('/delete/{id}')
def delete_sub_category(request, id):
    sub_category = get_object_or_404(SubCategory, id=id)
    sub_category.delete()
    return f"Sub Category {sub_category.name} deleted successfully"