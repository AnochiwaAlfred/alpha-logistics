from ninja import NinjaAPI, Schema
from ninja.security import django_auth
from ninja.security import HttpBearer
from authuser.models import CustomUser
from django.http import HttpResponseForbidden,response
from http import HTTPStatus


from apis.v1.agent import router as agent_router
from apis.v1.auth import router as auth_router
from apis.v1.categories import router as categories_router
from apis.v1.client import router as client_router
from apis.v1.dispatch import router as dispatch_router
from apis.v1.driver import router as driver_router
from apis.v1.orders import router as orders_router
from apis.v1.payments import router as payments_router
from apis.v1.products import router as products_router
from apis.v1.sub_categories import router as sub_categories_router
from apis.v1.tasks import router as tasks_router
from apis.v1.vendor import router as vendor_router

class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        # user =  User.objects.all().filter(encoded=token,is_token_verified=True)
        user =  CustomUser.objects.all().filter(encoded=token)
        if user.exists():
            foundUser = user.get()
            return foundUser.encoded
      
# api = NinjaAPI(auth=GlobalAuth())
api = NinjaAPI()


api.add_router("/agent/", agent_router)
api.add_router("/auth/", auth_router)
api.add_router("/categories/", categories_router)
api.add_router("/client/", client_router)
api.add_router("/dispatch/", dispatch_router)
api.add_router("/driver/", driver_router)
api.add_router("/orders/", orders_router)
api.add_router("/payments/", payments_router)
api.add_router("/products/", products_router)
api.add_router("/sub_categories/", sub_categories_router)
api.add_router("/tasks/", tasks_router)
api.add_router("/vendor/", vendor_router)



# class PaginationMetadata(Schema):
#     per_page: int
#     page: int
#     total: int
#     has_next: bool
#     has_previous: bool
#     pages: int