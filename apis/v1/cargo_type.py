from ninja import Router, Form
from django.shortcuts import get_object_or_404
from alpha_logistics.schemas.cargo_type import *
from cargo_types.models.cargo_type import *
from typing import List

router = Router(tags=['Cargo Types'])

@router.post('/add', response=CargoTypeOutSchema)
def add_cargo_type(request, data:CargoTypeInSchema=Form(...)):
    cargo_type = CargoType.objects.create(**data.dict())
    return cargo_type

@router.get('/cargo-type/{id}', response=CargoTypeOutSchema)
def get_cargo_type(request, id):
    cargo_type = get_object_or_404(CargoType, id=id)
    return cargo_type

@router.get('/list', response=List[CargoTypeOutSchema])
def list_cargo_types(request):
    d_list = CargoType.objects.all()
    return d_list

@router.put('/change/{id}', response=CargoTypeOutSchema)
def update_cargo_type(request, id, data:CargoTypeInSchema):
    cargo_type = get_object_or_404(CargoType, id=id)
    for attr, value in data.dict().items():
        setattr(cargo_type, attr, value)
    cargo_type.save()
    return cargo_type

@router.delete('/delete/{id}')
def delete_cargo_type(request, id):
    cargo_type = get_object_or_404(CargoType, id=id)
    cargo_type.delete()
    return f"Cargo Type {cargo_type.name} deleted successfully"