from ninja import NinjaAPI, Schema
from ninja_extra import NinjaExtraAPI
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.controller import NinjaJWTDefaultController
import helpers

api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)
api.add_router("/waitlists/", "waitlists.api.router")

class UserSchema(Schema):
    username: str
    is_authenticated: bool
    email: str = None

@api.get("/user", response=UserSchema, auth=helpers.api_auth_user_required)
def get_user(request):
    return request.user