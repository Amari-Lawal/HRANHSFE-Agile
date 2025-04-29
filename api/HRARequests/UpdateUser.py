from pydantic import BaseModel, Field,field_validator
from typing import Union,Literal,Optional
from datetime import datetime
from api.HRANHSExceptions import FieldNotExistException
import re
from api.HRANHSExceptions import InvalidPhoneNumberError
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
        
    @field_validator('phone_number')
    def validate_phone_number(cls, v):
        if v is None:
            return v  # Accept None
        # Match UK mobile numbers starting with 07 followed by 9 digits (total 11 digits)
        if not re.fullmatch(r'07\d{9}', v):
            raise InvalidPhoneNumberError(InvalidPhoneNumberError.message)
        return v
