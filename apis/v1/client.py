from ninja import Router, Form
from django.shortcuts import get_object_or_404
from alpha_logistics.schemas.auth import *
from authuser.models.user import *
from typing import List

router = Router(tags=['Client'])


@router.post('/add', response=ClientOutSchema)
def add_client(request, data:ClientInSchema=Form(...)):
    client = Client.objects.create(**data.dict())
    return client

@router.get('/client/{id}', response=ClientOutSchema)
def get_client(request, id):
    client = get_object_or_404(Client, id=id)
    return client

@router.get('/list', response=List[ClientOutSchema])
def list_clients(request):
    d_list = Client.objects.all()
    return d_list

@router.put('/change/{id}', response=ClientOutSchema)
def update_client(request, id, data:ClientInSchema):
    client = Client.objects.filter(id=id)[0]
    for attr, value in data.dict().items():
        setattr(client, attr, value)
    client.save()
    return client

@router.delete('/delete/{id}')
def delete_client(request, id):
    client = get_object_or_404(Client, id=id)
    client.delete()
    return f"Client {client.name} deleted successfully"