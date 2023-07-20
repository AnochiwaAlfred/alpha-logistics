from ninja import Schema
from alpha_logistics.schemas.auth import AuthOutSchema
from alpha_logistics.schemas.products import ProductOutSchema
import uuid

class OrderInSchema(Schema):
    client_id:str
    product_id:str
    quantity:int
    

class OrderOutSchema(Schema):
    id:uuid.UUID
    quantity:int
    client_id:AuthOutSchema=None
    product_id:ProductOutSchema=None
    
    # 10d272e0-f661-4b4a-9be4-693a14b0c862
    
    # 46218ecb-3410-4b24-8318-be408db0a194