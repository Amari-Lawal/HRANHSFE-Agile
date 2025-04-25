from pydantic import BaseModel, UUID4, HttpUrl, Field,computed_field
from typing import Optional, Union
from datetime import date, datetime
from decimal import Decimal
from typing import ClassVar
import uuid
from api.HRANHSExceptions import FieldNotExistException
from api.HRANHSDB import HRANHSCRUD
from api.HRAModels import Vendor
class UpdateMedicineAsset(BaseModel):
    medicine_asset: Optional[str] = None
    vendor_id: Optional[str] = None
    description:Optional[str] = None
    category:Optional[str] = None
    lot_number:Optional[str] = None
    manufacture_date: Optional[date] = None
    purchase_cost: Optional[float] = None
    storage_location:Optional[str] = None
    status:Optional[str] = None
    expiration_date: Optional[date] = None
    last_reviewed: Optional[date] = None
    next_review: Optional[date] = None
    storage_conditions:Optional[str] = None
    useful_life_years: Optional[int] = None
    current_stock: Optional[int] = None
    image_url: Optional[str] = None
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

