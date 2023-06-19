from ninja import Router
from django.shortcuts import get_object_or_404
from alpha_logistics.schemas.payments import *
from payments.models.payments import *
from authuser.models import User
from orders.models import Order
from typing import List

router = Router(tags=['Payments'])



@router.post('/add', response=PaymentOutSchema)
def add_payment(request, user_id, order_id):
    user = get_object_or_404(User, id=user_id)
    order = get_object_or_404(Order, id=order_id)
    payment = Payment.objects.create()
    payment.order_id = order
    payment.user_id = user
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
def update_payment(request, id, user_id=None, order_id=None):
    payment = get_object_or_404(Payment, id=id)
    if user_id!=None:
        user = get_object_or_404(User, id=user_id)
        payment.user_id=user
    if order_id!=None:
        order = get_object_or_404(Order, id=order_id)
        payment.order_id=order
    payment.save()
    return payment

@router.delete('/delete/{id}')
def delete_payment(request, id):
    payment = get_object_or_404(Payment, id=id)
    payment.delete()
    return f"Payment {payment.id} deleted successfully"
