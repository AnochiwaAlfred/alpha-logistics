from ninja import Schema
from alpha_logistics.schemas.auth import AuthOutSchema
from alpha_logistics.schemas.orders import OrderOutSchema
import uuid

class PaymentOutSchema(Schema):
    id:uuid.UUID
    order_id:OrderOutSchema=None
    user_id:AuthOutSchema=None