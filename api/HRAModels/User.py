from pydantic import BaseModel, computed_field, Field
from datetime import datetime
import uuid
from typing import Optional
import hashlib
from typing import ClassVar,Literal,Union
from api.HRANHSExceptions import FieldNotExistException
class User(BaseModel):
    USERSTABLENAME: ClassVar[str] = "users"
    user_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    first_name: str
    last_name: str
    email: str
    password: str
    role: Literal['admin', 'user']
    department: Optional[str] = None
    phone_number: Optional[str] = None
    status: str = "active"
    last_login: datetime = Field(default_factory=datetime.now)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    USERSDATATYPES: ClassVar[tuple] = (
            "TEXT PRIMARY KEY",      # user_id as UUID (VARCHAR(255) NOT NULL format)
            "VARCHAR(255) NOT NULL",                  # first_name as VARCHAR(255) NOT NULL
            "VARCHAR(255) NOT NULL",                  # last_name as VARCHAR(255) NOT NULL
            "VARCHAR(255) NOT NULL UNIQUE",           # email as unique VARCHAR(255) NOT NULL
            "VARCHAR(255) NOT NULL",                  # password_hash as VARCHAR(255) NOT NULL
            "VARCHAR(255) NOT NULL",                  # role as VARCHAR(255) NOT NULL
            "VARCHAR(255) NOT NULL",                  # department as VARCHAR(255) NOT NULL (optional)
            "VARCHAR(255) NOT NULL",                  # phone_number as VARCHAR(255) NOT NULL
            "VARCHAR(255) NOT NULL",                  # status as VARCHAR(255) NOT NULL
            "TIMESTAMP",             # last_login as TIMESTAMP
            "TIMESTAMP",             # created_at as TIMESTAMP
            "TIMESTAMP"              # updated_at as TIMESTAMP
        )
    
    @classmethod
    def fields_to_tuple(cls) -> tuple:
        return tuple(cls.model_fields)
    
    def values_to_tuple(self) -> tuple:
        return tuple(self.model_dump().values())
    @classmethod
    def get_field_name(cls,value) -> Union[str,None]:
        keys = list(cls.model_fields)
        if value in keys:
            return value
        else:
            raise FieldNotExistException(value)

class UserLogin(BaseModel):
    email:str
    password:str