
from ninja import Schema
import uuid

class CargoTypeInSchema(Schema):
    name:str
    description: str
    
class CargoTypeOutSchema(Schema):
    id:uuid.UUID
    name:str
    description:str