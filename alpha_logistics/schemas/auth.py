from ninja import Schema

    # IN SCHEMAS


class AuthInSchema(Schema):
    username:str
    email:str
    password: str


class AgentInSchema(AuthInSchema):
    first_name:str
    last_name:str
    address:str
    
    
class ClientInSchema(AuthInSchema):
    first_name:str
    address:str
    
    
class DriverInSchema(AuthInSchema):
    first_name:str
    last_name:str
    gender:str
    address:str
    
    
class VendorInSchema(AuthInSchema):
    first_name:str
    last_name:str
    address:str
    
    
    # OUT SCHEMAS
    
    
    
    
class AuthOutSchema(Schema):
    id:int
    username:str
    email:str
    password:str
    
    
class AgentOutSchema(AuthOutSchema):
    first_name:str
    last_name:str
    address:str
    
    
class ClientOutSchema(AuthOutSchema):
    first_name:str
    address:str
    
    
class DriverOutSchema(AuthOutSchema):
    first_name:str
    last_name:str
    gender:str
    address:str
    
    
class VendorOutSchema(AuthOutSchema):
    first_name:str
    last_name:str
    address:str