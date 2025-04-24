from pydantic import BaseModel, UUID4, HttpUrl, Field
from typing import Optional, Union
from datetime import date, datetime
from decimal import Decimal
from typing import ClassVar
import uuid
from HRANHSExceptions import FieldNotExistException
class VendorMedicineAsset(BaseModel):
    VENDORMEDICINEASSETSTABLENAME: ClassVar[str] = "vendormedicineasset"
    vendor_user_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    vendor_id: str 
    medicine_id: str

    VENDORMEDICINEASSETDATATYPES: ClassVar[tuple] = (
    "TEXT PRIMARY KEY",  # vendor_id as UUID (TEXT PRIMARY KEY format)
    "TEXT NOT NULL",  # vendor_name
    "TEXT NOT NULL",  # vendor_address
    "FOREIGN KEY (vendor_id) REFERENCES Vendor(vendor_id)",
    "FOREIGN KEY (medicine_id) REFERENCES MedicineAsset(medicine_id)"
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

