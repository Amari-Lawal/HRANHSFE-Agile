from pydantic import BaseModel
from api.HRAModels import User
class UserResponse(BaseModel):
    users: list[User]