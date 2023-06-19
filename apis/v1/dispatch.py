from ninja import Router
from django.shortcuts import get_object_or_404
from alpha_logistics.schemas.dispatch import *
from dispatch.models.dispatch import *
from tasks.models import Task
from typing import List

router = Router(tags=['Dispatch'])




@router.post('/add', response=DispatchOutSchema)
def add_dispatch(request, task_id):
    task_id = get_object_or_404(Task, id=task_id)
    dispatch = Dispatch.objects.create()
    dispatch.task_id=task_id
    dispatch.save()
    return dispatch

@router.get('/dispatch/{id}', response=DispatchOutSchema)
def get_dispatch(request, id):
    dispatch = get_object_or_404(Dispatch, id=id)
    return dispatch


@router.get('/list', response=List[DispatchOutSchema])
def list_dispatch(request):
    dispatchs = Dispatch.objects.all()
    return dispatchs


@router.put('/change/{id}', response=DispatchOutSchema)
def update_dispatch(request, id, task_id=None):
    dispatch = get_object_or_404(Dispatch, id=id)
    if task_id!=None:
        task_id = get_object_or_404(Task, id=task_id)
        dispatch.task_id=task_id
    dispatch.save()
    return dispatch

@router.delete('/delete/{id}')
def delete_dispatch(request, id):
    dispatch = get_object_or_404(Dispatch, id=id)
    dispatch.delete()
    return f"Dispatch {dispatch.id} deleted successfully"

