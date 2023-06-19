from ninja import Router
from django.shortcuts import get_object_or_404
from alpha_logistics.schemas.orders import *
from orders.models.orders import *
from products.models.products import Product
from authuser.models import User
from typing import List

router = Router(tags=['Orders'])

@router.post('/add', response=OrderOutSchema)
def add_order(request, user_id, product_id):
    user = get_object_or_404(User, id=user_id)
    product = get_object_or_404(Product, id=product_id)
    order = Order.objects.create()
    order.user_id = user
    order.product_id.add(product)
    order.save()
    return order

@router.get('/order/{id}', response=OrderOutSchema)
def get_order(request, id):
    order = get_object_or_404(Order, id=id)
    return order


@router.get('/list', response=List[OrderOutSchema])
def list_order(request):
    orders = Order.objects.all()
    return orders


@router.put('/change/{id}', response=OrderOutSchema)
def update_order(request, id, user_id=None, product_id=None):
    order = get_object_or_404(Order, id=id)
    if user_id!=None:
        user = get_object_or_404(User, id=user_id)
        order.user_id=user
    if product_id!=None:
        product = get_object_or_404(Product, id=product_id)
        order.product_id=product
    order.save()
    return order

@router.delete('/delete/{id}')
def delete_order(request, id):
    order = get_object_or_404(Order, id=id)
    order.delete()
    return f"Order {order.id} deleted successfully"
