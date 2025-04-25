from pydantic import BaseModel, Field
from typing import Union,Literal,Optional
from datetime import datetime
from api.HRANHSExceptions import FieldNotExistException

class UpdateUser(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    department: Optional[str] = None
    phone_number: Optional[str] = None
    status: Optional[str] = None
    updated_at: datetime = Field(default_factory=datetime.now)
    @classmethod
    def fields_to_tuple(cls) -> tuple:
        return tuple(cls.model_fields)
    
    
    def values_to_tuple(self) -> tuple:
        return tuple(self.model_dump().values())
    def fields_from_existing_to_tuple(self) -> tuple:
        return tuple(field for field, value in self.model_dump().items() if value is not None)
    def values_from_existing_to_tuple(self) -> tuple:
        return tuple(value for value in self.model_dump().values() if value is not None)
    @classmethod
    def get_field_name(cls,value) -> Union[str,None]:
        keys = list(cls.model_fields)
        if value in keys:
            return value
        else:
            raise FieldNotExistException(value)

