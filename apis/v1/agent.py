from ninja import Router, Form
from django.shortcuts import get_object_or_404
from alpha_logistics.schemas.auth import *
from authuser.models.user import *
from typing import List

router = Router(tags=['Agents'])


@router.post('/add', response=AgentOutSchema)
def add_agent(request, data:AgentInSchema=Form(...)):
    new_data = data.dict()
    password = str(new_data.pop('password'))
    agent = Agent.objects.create(**new_data)
    agent.set_password(password)
    agent.save()
    return agent

@router.get('/agent/{id}', response=AgentOutSchema)
def get_agent(request, id):
    agent = get_object_or_404(Agent, id=id)
    return agent

@router.get('/list', response=List[AgentOutSchema])
def list_agents(request):
    d_list = Agent.objects.all()
    return d_list

@router.put('/change/{id}', response=AgentOutSchema)
def update_agent(request, id, data:AgentInSchema):
    agent = Agent.objects.filter(id=id)[0]
    for attr, value in data.dict().items():
        setattr(agent, attr, value)
    agent.save()
    return agent

@router.delete('/delete/{id}')
def delete_agent(request, id):
    agent = get_object_or_404(Agent, id=id)
    agent.delete()
    return f"Agent {agent.name} deleted successfully"