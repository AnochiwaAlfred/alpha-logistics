from ninja import Router, Form
from django.shortcuts import get_object_or_404
from alpha_logistics.schemas.tasks import *
from tasks.models.tasks import *
from authuser.models import Driver
from orders.models import Order
from typing import List

router = Router(tags=['Tasks'])



@router.post('/add', response=TaskOutSchema)
def add_task(request, data:TaskInSchema=Form(...)):
    driver_id = get_object_or_404(Driver, id=int(data.dict().get('driver_id')))
    task = Task.objects.create()
    task.driver_id=driver_id
    task.save()
    list_in = data.dict().get('order_id')[0].split(',')
    for item in list_in:
        order_id = Order.objects.filter(id=item)[0]
        task.order_id.add(order_id)
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
def update_task(request, id,  data:TaskInSchema):
    task = Task.objects.filter(id=id)[0]
    driver_id = get_object_or_404(Driver, id=int(data.dict().get('driver_id')))
    task.driver_id=driver_id
    task.save()
    list_in = data.dict().get('order_id')[0].split(',')
    for item in list_in:
        order_id = Order.objects.filter(id=item)[0]
        task.order_id.add(order_id)
    task.save() 
    return task

@router.delete('/delete/{id}')
def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return f"Task deleted successfully"
