
from ninja import Schema
import uuid
from alpha_logistics.schemas.tasks import TaskOutSchema

class DispatchOutSchema(Schema):
    id:uuid.UUID
    task_id:TaskOutSchema=None