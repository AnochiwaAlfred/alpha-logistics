from ninja import Schema
from alpha_logistics.schemas.auth import AuthOutSchema
from alpha_logistics.schemas.categories import CategoryOutSchema
import uuid    

class ProductInSchema(Schema):
    name:str
    description:str
    weight:int
        
        
class ProductOutSchema(Schema):
    id:uuid.UUID
    name:str
    description:str
    user_id:AuthOutSchema
    category_id:CategoryOutSchema
    weight:int