# CLAUDE.md

## Section 1: Project Overview

**App Name**: Beach Bum Rentals  
**Description**: This application manages the rental process for beach equipment, handling inventory, checkouts, and returns. It replaces manual processes with an automated system for tracking equipment availability and rental history.  
**Entities**:
- Beach Equipment
- Checkouts

**Workflows**:
- Rental Process

## Section 2: Tech Stack

- **Backend**: Python 3.11, FastAPI, Pydantic v2, SQLAlchemy 2.0, SQLite
- **Frontend**: React 19, TypeScript, Vite, TailwindCSS, shadcn/ui

## Section 3: Data Models

```python
from enum import Enum
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float, Enum as SQLAEnum, Date, ForeignKey
from sqlalchemy.orm import declarative_base
from typing import Optional
from datetime import datetime

Base = declarative_base()

# Enums
class CheckoutStatus(str, Enum):
    pending = 'pending'
    checked_out = 'checked_out'
    returned = 'returned'
    cancelled = 'cancelled'

# SQLAlchemy Models
class Equipment(Base):
    __tablename__ = 'x_beachbum_equipment'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    available_quantity = Column(Integer, nullable=False)
    condition = Column(String, nullable=False)
    daily_rate = Column(Float, nullable=False)

class Checkout(Base):
    __tablename__ = 'x_beachbum_checkout'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    equipment_id = Column(Integer, ForeignKey('x_beachbum_equipment.id'), nullable=False)
    customer_name = Column(String, nullable=False)
    customer_email = Column(String, nullable=False)
    rental_start = Column(Date, nullable=False)
    rental_end = Column(Date, nullable=False)
    return_date = Column(Date, nullable=True)
    status = Column(SQLAEnum(CheckoutStatus), default=CheckoutStatus.pending)
    notes = Column(String, nullable=True)
    created_at = Column(Date, default=datetime.utcnow)
    updated_at = Column(Date, onupdate=datetime.utcnow)

# Pydantic Models
class EquipmentModel(BaseModel):
    id: int
    available_quantity: int
    condition: str
    daily_rate: float

class CheckoutModel(BaseModel):
    id: int
    equipment_id: int
    customer_name: str
    customer_email: str
    rental_start: datetime
    rental_end: datetime
    return_date: Optional[datetime] = None
    status: CheckoutStatus = CheckoutStatus.pending
    notes: Optional[str] = None
    created_at: datetime
    updated_at: datetime

class CreateCheckoutModel(BaseModel):
    equipment_id: int
    customer_name: str
    customer_email: str
    rental_start: datetime
    rental_end: datetime
    notes: Optional[str] = None

class UpdateCheckoutStatusModel(BaseModel):
    status: CheckoutStatus

```

## Section 4: API Endpoints

```python
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

router = APIRouter()

@router.get('/equipment', response_model=list[EquipmentModel])
async def list_equipment(db: Session = Depends(get_db)):
    ...

@router.get('/checkouts', response_model=list[CheckoutModel])
async def list_checkouts(status: CheckoutStatus | None = None, db: Session = Depends(get_db)):
    ...

@router.post('/checkouts', response_model=CheckoutModel)
async def create_checkout(body: CreateCheckoutModel, db: Session = Depends(get_db)):
    ...

@router.post('/checkouts/{id}/return', response_model=CheckoutModel)
async def return_checkout(id: int, db: Session = Depends(get_db)):
    ...

```

## Section 5: Business Logic

```python
async def decrement_inventory(db: Session, equipment_id: int, qty: int = 1) -> Equipment:
    '''Reduce available_quantity when checkout is created.
    Raises ValueError if qty > available_quantity.'''
    ...

async def restore_inventory(db: Session, equipment_id: int, qty: int = 1) -> Equipment:
    '''Increase available_quantity when checkout is returned.'''
    ...
```

## Section 6: Workflows

```python
from typing import List

class Step:
    def __init__(self, step: str, actor: str, action: str, validates: List[str] = [], calls: List[str] = [], emits: str = ""):
        self.step = step
        self.actor = actor
        self.action = action
        self.validates = validates
        self.calls = calls
        self.emits = emits

RENTAL_WORKFLOW = [
    Step('request', actor='customer', action='submit_rental_form',
         validates=['equipment_available'], emits='checkout_created'),
    Step('checkout', actor='system', action='create_checkout_record',
         calls=['decrement_inventory']),
    Step('return', actor='customer', action='mark_returned',
         calls=['restore_inventory'], emits='equipment_returned'),
]
```

## Section 7: Event Handlers

```python
@on_event('checkout_created')
async def on_checkout_created(checkout: Checkout, db: Session):
    await decrement_inventory(db, checkout.equipment_id)

@on_event('equipment_returned')
async def on_equipment_returned(checkout: Checkout, db: Session):
    await restore_inventory(db, checkout.equipment_id)
```

## Section 8: UI Pages

```
Active Checkouts fields:
  status: Enum, required (status=checked_out)

RentalRequestForm fields:
  customer_name:    TextInput, required
  customer_email:   EmailInput, required
  equipment_id:     Select (GET /api/equipment?available=true), required
  rental_start:     DatePicker, required
  rental_end:       DatePicker, required, must be after rental_start
  notes:            Textarea, optional
```

## Section 9: Navigation

- **Beach Bum**
  - All Equipment
  - All Checkouts
  - Active Checkouts
  - Add Equipment

## Section 10: Architecture Rules

- Entity pattern: models.py → database.py → services/{name}.py → routers/{name}.py
- All routes return {status, data} envelope
- Business logic lives in services/, never in routers
- DB session via FastAPI Depends(get_db)

## Section 11: Build Order

1. Scaffold: create backend/ and frontend/ with venv + package.json
2. backend/models.py — all Pydantic models and enums from Section 3
3. backend/database.py — SQLAlchemy engine + Base + get_db + create_tables()
4. backend/services/{entity}.py — all service functions from Section 5
5. backend/workflows.py — Step dataclass + workflow definitions from Section 6
6. backend/events.py — event bus + handlers from Section 7
7. backend/routers/{entity}.py — all FastAPI routes from Section 4
8. backend/main.py — app factory, CORS, lifespan (create_tables), router includes
9. frontend/src/api/ — typed fetch hooks for each endpoint
10. frontend/src/pages/ — all pages from Section 8
11. Run seed.json through POST endpoints to populate the DB