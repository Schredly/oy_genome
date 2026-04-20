from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BeachRentalBase(BaseModel):
    rental_duration: int
    customer_name: str
    rental_type: str

class BeachRentalCreate(BeachRentalBase):
    pass

class BeachRentalUpdate(BaseModel):
    rental_duration: Optional[int] = None
    rental_type: Optional[str] = None

class BeachRental(BeachRentalBase):
    sys_id: str
    created_on: datetime
    created_by: str
    updated_on: datetime
    updated_by: str

    class Config:
        orm_mode = True

class Customer(BaseModel):
    sys_id: str
    name: str

    class Config:
        orm_mode = True