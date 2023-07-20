from ninja import Schema
from alpha_logistics.schemas.categories import CategoryOutSchema
import uuid    

class SubCategoryInSchema(Schema):
    name:str
    description:str
    category_id:str
    is_active:bool
        
        
class SubCategoryOutSchema(Schema):
    id:uuid.UUID
    name:str
    description:str
    category:CategoryOutSchema
    is_active:bool