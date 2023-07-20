from ninja import Router, Form
from django.shortcuts import get_object_or_404
from alpha_logistics.schemas.orders import *
from orders.models.orders import *
from products.models.products import Product
from authuser.models import *
from typing import List

router = Router(tags=['Orders'])

@router.post('/add', response=OrderOutSchema)
def add_order(request, data:OrderInSchema=Form(...)):
    client_id = get_object_or_404(Client, id=int(data.dict().get('client_id')))
    product_id = get_object_or_404(Product, id=uuid.UUID(data.dict().get('product_id')))
    order = Order.objects.create(quantity=data.dict().get('quantity'))
    order.client_id = client_id
    order.product_id = product_id
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
def update_order(request, id, data:OrderInSchema):
    order = Order.objects.filter(id=id)[0]
    client_id = get_object_or_404(Client, id=int(data.dict().get('client_id')))
    product_id = get_object_or_404(Product, id=uuid.UUID(data.dict().get('product_id')))
    order.quantity = data.dict().get('quantity')
    order.client_id = client_id
    order.product_id = product_id
    order.save()
    order.save()
    return order

@router.delete('/delete/{id}')
def delete_order(request, id):
    order = get_object_or_404(Order, id=id)
    order.delete()
    return f"Order {order.id} deleted successfully"
