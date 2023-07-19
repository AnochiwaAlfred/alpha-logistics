from ninja import NinjaAPI
from ninja.security import django_auth
from ninja.security import HttpBearer
from authuser.models import CustomUser
from django.http import HttpResponseForbidden,response
from http import HTTPStatus


from apis.v1.auth import router as auth_router
from apis.v1.cargo_type import router as cargo_type_router
from apis.v1.categories import router as categories_router
from apis.v1.dispatch import router as dispatch_router
from apis.v1.kyc import router as kyc_router
from apis.v1.orders import router as orders_router
from apis.v1.payments import router as payments_router
from apis.v1.products import router as products_router
from apis.v1.tasks import router as tasks_router

class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        # user =  User.objects.all().filter(encoded=token,is_token_verified=True)
        user =  CustomUser.objects.all().filter(encoded=token)
        if user.exists():
            foundUser = user.get()
            return foundUser.encoded
      
api = NinjaAPI(auth=GlobalAuth())
<<<<<<< HEAD
# api = NinjaAPI()
=======
>>>>>>> 70aa3c70037c5afd227373c14d0fbb16dc7b7a59


api.add_router("/auth/", auth_router)
api.add_router("/cargo-type/", cargo_type_router)
api.add_router("/categories/", categories_router)
api.add_router("/dispatch/", dispatch_router)
api.add_router("/kyc/", kyc_router)
api.add_router("/orders/", orders_router)
api.add_router("/payments/", payments_router)
api.add_router("/products/", products_router)
api.add_router("/tasks/", tasks_router)



