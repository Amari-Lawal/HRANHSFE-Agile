from pydantic import BaseModel, UUID4, HttpUrl, Field
from typing import Optional, Union
from datetime import date, datetime
from decimal import Decimal
from typing import ClassVar
import uuid
class Asset(BaseModel):
    ASSETSTABLENAME: ClassVar[str] = "assets"
    asset_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    asset_name: str
    description: Optional[str] = None
    category: Optional[str] = None
    serial_number: Optional[str] = None
    purchase_date: Optional[date] = None
    purchase_cost: Optional[Decimal] = None
    vendor: Optional[str] = None
    location: Optional[str] = None
    status: Optional[str] = None
    warranty_expiry: Optional[date] = None
    last_maintenance: Optional[date] = None
    next_maintenance: Optional[date] = None
    depreciation_method: Optional[str] = None
    useful_life_years: Optional[int] = None
    current_value: Optional[Decimal] = None
    image_url: Optional[Union[HttpUrl, str]] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    USERSDATATYPES: ClassVar[tuple] = (
    "TEXT NOT NULL",         # asset_id (UUID / INT → VARCHAR(255) NOT NULL for UUID or INTEGER if you separate them)
    "VARCHAR(255) NOT NULL",         # asset_name (VARCHAR)
    "VARCHAR(255) NOT NULL",         # description (VARCHAR(255) NOT NULL)
    "VARCHAR(255) NOT NULL",         # category (VARCHAR)
    "TEXT NOT NULL",         # serial_number (VARCHAR)
    "DATE",         # purchase_date (DATE)
    "REAL",         # purchase_cost (DECIMAL(10,2) → REAL in SQLite)
    "VARCHAR(255) NOT NULL",         # vendor (VARCHAR)
    "VARCHAR(255) NOT NULL",         # location (VARCHAR)
    "VARCHAR(255) NOT NULL",         # status (VARCHAR)
    "DATE",         # warranty_expiry (DATE)
    "DATE",         # last_maintenance (DATE)
    "DATE",         # next_maintenance (DATE)
    "VARCHAR(255)",         # depreciation_method (VARCHAR)
    "INTEGER",      # useful_life_years (INT)
    "REAL",         # current_value (DECIMAL(10,2))
    "TEXT NOT NULL",         # image_url (VARCHAR / VARCHAR(255) NOT NULL)
    "TIMESTAMP",    # created_at (TIMESTAMP)
    "TIMESTAMP",    # updated_at (TIMESTAMP)
)
    
    @classmethod
    def fields_to_tuple(cls) -> tuple:
        return tuple(cls.model_fields)
    
    def values_to_tuple(self) -> tuple:
        return tuple(self.model_dump().values())
