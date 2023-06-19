from ninja import Schema
from alpha_logistics.schemas.auth import AuthOutSchema
from alpha_logistics.schemas.products import ProductOutSchema
import uuid

class OrderOutSchema(Schema):
    id:uuid.UUID
    user_id:AuthOutSchema=None
    # product_id:ProductOutSchema=None
    