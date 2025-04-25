from pydantic import BaseModel, Field
from typing import Union
from datetime import datetime
from api.HRANHSExceptions import FieldNotExistException

class UpdateVendor(BaseModel):
    vendor_name: str 
    vendor_address: str
    contact_person: str
    contact_number: str
    email: str
    status: str
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

