from pydantic import BaseModel, UUID4, HttpUrl, Field
from typing import Optional, Union
from datetime import date, datetime
from decimal import Decimal
from typing import ClassVar
import uuid
from api.HRANHSExceptions import FieldNotExistException
class Vendor(BaseModel):
    VENDORTABLENAME: ClassVar[str] = "vendors"
    vendor_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    vendor_name: str 
    vendor_address: str
    contact_person: str
    contact_number: str
    email: str
    status: str = Field(default="active")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    VENDORDATATYPES: ClassVar[tuple] = (
    "TEXT PRIMARY KEY",  # vendor_id as UUID (TEXT PRIMARY KEY format)
    "VARCHAR(255) NOT NULL",  # vendor_name
    "VARCHAR(255) NOT NULL",  # vendor_address
    "VARCHAR(255) NOT NULL",  # contact_person
    "VARCHAR(255) NOT NULL",  # contact_number
    "VARCHAR(255) NOT NULL",  # email
    "VARCHAR(255) NOT NULL",  # status
    "DATETIME",  # created_at
    "DATETIME",  # updated_at

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

