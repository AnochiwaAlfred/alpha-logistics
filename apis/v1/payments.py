from ninja import Router, Form
from django.shortcuts import get_object_or_404
from alpha_logistics.schemas.payments import *
from payments.models.payments import *
from authuser.models import Client
from orders.models import Order
from typing import List

router = Router(tags=['Payments'])



@router.post('/add', response=PaymentOutSchema)
def add_payment(request, data:PaymentInSchema=Form(...)):
    order_id = Order.objects.filter(id=data.dict().get('order_id'))[0]
    payment = Payment.objects.create()
    payment.order_id = order_id
    payment.save()
    return payment

@router.get('/payment/{id}', response=PaymentOutSchema)
def get_payment(request, id):
    payment = get_object_or_404(Payment, id=id)
    return payment


@router.get('/list', response=List[PaymentOutSchema])
def list_payment(request):
    payments = Payment.objects.all()
    return payments


@router.put('/change/{id}', response=PaymentOutSchema)
def update_payment(request, id, data:PaymentInSchema):
    order_id = Order.objects.filter(id=data.dict().get('order_id'))[0]
    payment = Payment.objects.filter(id=id)
    payment.order_id = order_id
    payment.save()
    return payment

@router.delete('/delete/{id}')
def delete_payment(request, id):
    payment = get_object_or_404(Payment, id=id)
    payment.delete()
    return f"Payment {payment.id} deleted successfully"
