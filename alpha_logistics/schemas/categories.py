
from ninja import Schema, Form
import uuid

class CategoryInSchema(Schema):
    name:str
    description:str
    
class CategoryOutSchema(Schema):
    id:uuid.UUID
    name:str
    description:str
    is_active:bool