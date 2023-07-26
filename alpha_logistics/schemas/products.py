from ninja import Schema
from alpha_logistics.schemas.auth import *
from alpha_logistics.schemas.sub_categories import SubCategoryOutSchema
import uuid    

class ProductInSchema(Schema):
    name:str
    description:str
    vendor_id:int
    sub_category_id:str
    price:float
    is_available:bool
    
        
        
class ProductOutSchema(Schema):
    id:uuid.UUID
    name:str
    description:str
    vendor_id:VendorOutSchema
    sub_category_id:SubCategoryOutSchema
    price:float
    is_available:bool
    