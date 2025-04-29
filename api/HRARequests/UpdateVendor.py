from pydantic import BaseModel, Field,field_validator
from typing import Union,Optional
from datetime import datetime
from api.HRANHSExceptions import FieldNotExistException,InvalidPhoneNumberError
import re
class UpdateVendor(BaseModel):
    vendor_name: Optional[str] = None 
    vendor_address: Optional[str] = None
    contact_person: Optional[str] = None
    contact_number: Optional[str] = None
    email: Optional[str] = None
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

    @field_validator('contact_number')
    def validate_contact_number(cls, v):
        if v is None:
            return v  # Accept None
        uk_phone_regex = re.compile(InvalidPhoneNumberError.regex)
        if not uk_phone_regex.fullmatch(v):
            raise InvalidPhoneNumberError(InvalidPhoneNumberError.message)
        return v
