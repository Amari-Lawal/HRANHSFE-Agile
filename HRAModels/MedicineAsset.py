from pydantic import BaseModel, UUID4, HttpUrl, Field
from typing import Optional, Union
from datetime import date, datetime
from decimal import Decimal
from typing import ClassVar
import uuid
from HRANHSExceptions import FieldNotExistException
class MedicineAsset(BaseModel):
    MEDICINEASSETSTABLENAME: ClassVar[str] = "medical_assets"
    drug_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    drug_name: str
    description: str
    category: str
    lot_number: str
    manufacture_date: date
    purchase_cost: float
    vendor: str
    storage_location: str
    status: str
    expiration_date: date
    last_reviewed: Optional[date] = None
    next_review: Optional[date] = None
    storage_conditions: str
    useful_life_years: int
    current_stock: int
    image_url: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    MEDICINEASSETDATATYPES: ClassVar[tuple] = (
    "TEXT PRIMARY KEY",  # drug_id as UUID (VARCHAR(255) NOT NULL format)
    "VARCHAR(255) NOT NULL",  # drug_name
    "VARCHAR(255) NOT NULL",  # description
    "VARCHAR(255) NOT NULL",  # category
    "VARCHAR(255) NOT NULL",  # lot_number
    "DATE NOT NULL",          # manufacture_date
    "REAL NOT NULL",          # purchase_cost
    "VARCHAR(255) NOT NULL",  # vendor
    "VARCHAR(255) NOT NULL",  # storage_location
    "VARCHAR(255) NOT NULL",  # status
    "DATE NOT NULL",          # expiration_date
    "DATE",                   # last_reviewed (nullable)
    "DATE",                   # next_review (nullable)
    "VARCHAR(255) NOT NULL",  # storage_conditions
    "INTEGER NOT NULL",       # useful_life_years
    "INTEGER NOT NULL",       # current_stock
    "VARCHAR(255)",            # image_url (nullable)
    "TIMESTAMP",    # created_at (TIMESTAMP)
    "TIMESTAMP",    # updated_at (TIMESTAMP)
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

