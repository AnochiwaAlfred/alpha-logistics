from ninja import Schema

class AuthOutSchema(Schema):
    id:int
    username:str
    email:str