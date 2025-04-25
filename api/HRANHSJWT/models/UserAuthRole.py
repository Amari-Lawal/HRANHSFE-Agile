from pydantic import BaseModel

class UserAuthRole(BaseModel):
    email:str
    role:str