from ninja import Router, Form
from django.shortcuts import get_object_or_404
from alpha_logistics.schemas.auth import *
from authuser.models.user import *
from typing import List

router = Router(tags=['Drivers'])


@router.post('/add', response=DriverOutSchema)
def add_driver(request, data:DriverInSchema=Form(...)):
    driver = Driver.objects.create(**data.dict())
    return driver

@router.get('/driver/{id}', response=DriverOutSchema)
def get_driver(request, id):
    driver = get_object_or_404(Driver, id=id)
    return driver

@router.get('/list', response=List[DriverOutSchema])
def list_drivers(request):
    d_list = Driver.objects.all()
    return d_list

@router.put('/change/{id}', response=DriverOutSchema)
def update_driver(request, id, data:DriverInSchema):
    driver = Driver.objects.filter(id=id)[0]
    for attr, value in data.dict().items():
        setattr(driver, attr, value)
    driver.save()
    return driver

@router.delete('/delete/{id}')
def delete_driver(request, id):
    driver = get_object_or_404(Driver, id=id)
    driver.delete()
    return f"Driver {driver.name} deleted successfully"