from ninja import Router
from django.shortcuts import get_object_or_404
from alpha_logistics.schemas.tasks import *
from tasks.models.tasks import *
from cargo_types.models import CargoType
from orders.models import Order
from typing import List

router = Router(tags=['Tasks'])



@router.post('/add', response=TaskOutSchema)
def add_task(request, cargo_type_id, order_id):
    cargo_type = get_object_or_404(CargoType, id=cargo_type_id)
    order = get_object_or_404(Order, id=order_id)
    task = Task.objects.create()
    task.order_id.add(order)
    task.cargo_type=cargo_type
    task.save()
    return task

@router.get('/task/{id}', response=TaskOutSchema)
def get_task(request, id):
    task = get_object_or_404(Task, id=id)
    return task


@router.get('/list', response=List[TaskOutSchema])
def list_task(request):
    tasks = Task.objects.all()
    return tasks


@router.put('/change/{id}', response=TaskOutSchema)
def update_task(request, id, cargo_type_id=None, order_id=None):
    task = get_object_or_404(Task, id=id)
    if cargo_type_id!=None:
        cargo_type = get_object_or_404(CargoType, id=cargo_type_id)
        task.cargo_type=cargo_type
    if order_id!=None:
        order = get_object_or_404(Order, id=order_id)
        task.order_id.add(order)
    task.save()
    return task

@router.delete('/delete/{id}')
def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return f"task {task.id} deleted successfully"
