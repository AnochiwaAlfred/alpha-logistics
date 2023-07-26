
from ninja import Schema
import uuid
from alpha_logistics.schemas.orders import OrderOutSchema
from alpha_logistics.schemas.auth import *
from typing import List


class TaskInSchema(Schema):
    order_id:List[str]
    driver_id:str

class TaskOutSchema(Schema):
    id:uuid.UUID
    order_id:List[OrderOutSchema]=None
    driver_id:DriverOutSchema=None
    
