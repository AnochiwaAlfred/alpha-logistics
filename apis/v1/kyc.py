from ninja import Router, Form
from django.shortcuts import get_object_or_404
from alpha_logistics.schemas.kyc import *
from kyc.models.kyc import *
from authuser.models import CustomUser
from typing import List
from django_countries import countries

router = Router(tags=['KYC'])

COUNTRY_LIST =  [name for code, name in countries]
COUNTRY_REVERSE_DICT = {name:code for code, name in countries}

@router.post('/add', response=KYCOutSchema)
def add_kyc(request, user_id, data:KYCInSchema=Form(...)):
    user = get_object_or_404(CustomUser, id=user_id)
    client = KYC.objects.create(**data.dict())
    context = {}
    context.update(**data.dict())
    country = str(context.get('country')).title()
    country_code = COUNTRY_REVERSE_DICT.get(country)
    client.user_id=user
    client.save()
    if country in COUNTRY_LIST:
        client.country=country_code
        client.save()
        return client
    else:
        return {False: 'Country not valid'}
    
@router.get('/list', response=List[KYCOutSchema])
def list_KYC(request):
    clients = KYC.objects.all()
    return clients

@router.get('/kyc/{id}', response=KYCOutSchema)
def get_KYC(request, id):
    client = get_object_or_404(KYC, id=id)
    return client

@router.put('/change/{id}', response=KYCOutSchema)
def update_KYC(request, id, user_id, data:KYCInSchema):
    user = get_object_or_404(CustomUser, id=user_id)
    client = get_object_or_404(KYC, id=id)
    for attr, value in data.dict().items():
        setattr(client, attr, value)
    context = {}
    context.update(**data.dict())
    country = str(context.get('country')).title()
    country_code = COUNTRY_REVERSE_DICT.get(country)
    client.user_id=user
    client.save()
    if country in COUNTRY_LIST:
        client.country=country_code
        client.save()
        return client
    else:
        return {False: 'Country not valid'}


@router.delete('/delete/{id}')
def delete_KYC(request, id):
    client = get_object_or_404(KYC, id=id)
    client.delete()
    return f"Client {client.first_name} {client.last_name} has been deleted sucessfully. \
        Associated user still remains."