from ninja import Schema
from alpha_logistics.schemas.auth import AuthOutSchema
import uuid

    
class KYCInSchema(Schema):
    first_name:str
    last_name:str
    country:str
    state:str
    city:str

        
        
class KYCOutSchema(Schema):
    id:uuid.UUID
    user_id:AuthOutSchema
    first_name:str
    last_name:str
    country:str
    state:str
    city:str
