
from ninja import Schema
import uuid
from alpha_logistics.schemas.orders import OrderOutSchema
from alpha_logistics.schemas.cargo_type import CargoTypeOutSchema
from typing import List

class TaskOutSchema(Schema):
    id:uuid.UUID
    order_id:List[OrderOutSchema]=None
    cargo_type:CargoTypeOutSchema=None
    
