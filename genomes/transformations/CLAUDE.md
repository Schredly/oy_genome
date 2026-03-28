# CLAUDE.md

## Section 1: Project Overview

The Beach Bum2 application is designed to facilitate the rental process of beach equipment. It replaces any legacy systems or manual processes previously used for managing beach rentals. The application manages beach items, processes rentals, calculates discounts, and updates inventory accordingly.

### Entities
- Beach Item
- Rental

### Workflows
- Equipment Rental Process
- Inventory Checkout
- Equipment Return

## Section 2: Tech Stack

- **Backend**: Python 3.11, FastAPI, Pydantic v2, SQLAlchemy 2.0, SQLite
- **Frontend**: React 19, TypeScript, Vite, TailwindCSS, shadcn/ui

## Section 3: Data Models — WRITE ACTUAL PYTHON CODE

```python
from enum import Enum
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, condecimal
from sqlalchemy import Column, String, DateTime, ForeignKey, Enum as SQLAEnum, DECIMAL
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CategoryChoice(str, Enum):
    CATEGORY_1 = "Category 1"
    CATEGORY_2 = "Category 2"

class EquipmentTypeChoice(str, Enum):
    SURFBOARD = "Surfboard"
    KAYAK = "Kayak"
    UMBRELLA = "Umbrella"

class BeachItem(Base):
    __tablename__ = 'beach_items'
    sys_id = Column(String, primary_key=True)
    created_on = Column(DateTime, default=datetime.utcnow)
    created_by = Column(String)
    updated_on = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    updated_by = Column(String)
    name = Column(String, nullable=False)
    category = Column(SQLAEnum(CategoryChoice))
    price = Column(DECIMAL, nullable=False)

class BeachItemModel(BaseModel):
    sys_id: str
    created_on: datetime
    created_by: str
    updated_on: datetime
    updated_by: str
    name: str = Field(..., description="The name of the beach item")
    category: CategoryChoice
    price: condecimal(max_digits=10, decimal_places=2)

class CreateBeachItem(BaseModel):
    name: str
    category: CategoryChoice
    price: condecimal(max_digits=10, decimal_places=2)

class UpdateBeachItem(BaseModel):
    name: Optional[str] = None
    category: Optional[CategoryChoice] = None
    price: Optional[condecimal(max_digits=10, decimal_places=2)] = None
```

## Section 4: API Endpoints — WRITE ACTUAL FASTAPI SIGNATURES

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()

@router.get('/beach_items', response_model=list[BeachItemModel])
async def list_beach_items(db: Session = Depends(get_db)): ...

@router.post('/beach_items', response_model=BeachItemModel)
async def create_beach_item(body: CreateBeachItem, db: Session = Depends(get_db)): ...

@router.put('/beach_items/{sys_id}', response_model=BeachItemModel)
async def update_beach_item(sys_id: str, body: UpdateBeachItem, db: Session = Depends(get_db)): ...

@router.delete('/beach_items/{sys_id}', status_code=204)
async def delete_beach_item(sys_id: str, db: Session = Depends(get_db)): ...
```

## Section 5: Business Logic — WRITE ACTUAL FUNCTION SIGNATURES

```python
async def calculate_discount(item_price: float, rental_days: int) -> float:
    '''Apply a 10% discount for rentals over 3 days.'''
    if rental_days > 3:
        return item_price * 0.9
    return item_price

async def decrement_inventory(db: Session, item_id: str, qty: int = 1) -> BeachItem:
    '''Reduce available_quantity when item is reserved.
    Raises ValueError if qty exceeds available inventory.'''
    ...

async def restore_inventory(db: Session, item_id: str, qty: int = 1) -> BeachItem:
    '''Increase available_quantity when item is returned.'''
    ...
```

## Section 6: Workflows

```python
EQUIPMENT_RENTAL_WORKFLOW = [
    Step('request', actor='customer', action='submit_rental_form', validates=['equipment_type is not empty'], emits='checkout_created'),
    Step('availability', actor='system', action='check_availability', calls=['decrement_inventory']),
    Step('reserve', actor='system', action='reserve_equipment'),
    Step('confirmation', actor='system', action='send_confirmation_email'),
]

INVENTORY_CHECKOUT_WORKFLOW = [
    Step('initiate', actor='customer', action='fill_rental_form', emits='initiate_checkout'),
    Step('availability', actor='system', action='check_availability', calls=['decrement_inventory']),
    Step('payment', actor='customer', action='process_payment'),
    Step('update', actor='system', action='decrement_inventory', calls=['decrement_inventory']),
]

EQUIPMENT_RETURN_WORKFLOW = [
    Step('initiate', actor='customer', action='return_item', emits='item_returned'),
    Step('confirm', actor='system', action='check_item_return', calls=['restore_inventory']),
    Step('update', actor='system', action='restore_inventory', calls=['restore_inventory']),
    Step('close', actor='system', action='finalize_return', emits='transaction_closed'),
]
```

## Section 7: Event Handlers

```python
@on_event('checkout_created')
async def on_checkout_created(beach_item: BeachItemModel, db: Session):
    await decrement_inventory(db, beach_item.sys_id)

@on_event('item_returned')
async def on_item_returned(beach_item: BeachItemModel, db: Session):
    await restore_inventory(db, beach_item.sys_id)
```

## Section 8: UI Pages

- **Beach Items List**
  - **Route**: `/beach-items`
  - **Component**: `BeachItemsList`
  - **Data Source**: `GET /api/beach_items`
  - **Key Features**: Display list of beach items, filter by category

- **Item Form**
  - **Route**: `/beach-items/{id}`
  - **Component**: `ItemForm`
  - **Data Source**: `GET /api/beach_items/{id}`
  - **Key Features**: Edit existing items, form validation

### Rental Form Fields
- **equipment_type**: Select, required, choices: ["Surfboard", "Kayak", "Umbrella"]
- **rental_days**: Numeric, required, validation for positive integer

## Section 9: Navigation

Map genome navigation.menu directly to sidebar routes and icons.

- **Main Menu**
  - - Beach Items List
  - - Item Form

## Section 10: Architecture Rules

- **Entity pattern**: `models.py` → `database.py` → `services/{name}.py` → `routers/{name}.py`
- All routes return `{status, data}` envelope
- Business logic lives in `services/`, never in `routers`
- DB session via FastAPI `Depends(get_db)`

## Section 11: Build Order

1. Scaffold: create `backend/` and `frontend/` with `venv` + `package.json`
2. `backend/models.py` — all Pydantic models and enums from Section 3
3. `backend/database.py` — SQLAlchemy engine + Base + `get_db` + `create_tables()`
4. `backend/services/{entity}.py` — all service functions from Section 5
5. `backend/workflows.py` — `Step` dataclass + workflow definitions from Section 6
6. `backend/events.py` — event bus + handlers from Section 7
7. `backend/routers/{entity}.py` — all FastAPI routes from Section 4
8. `backend/main.py` — app factory, CORS, lifespan (`create_tables`), router includes
9. `frontend/src/api/` — typed fetch hooks for each endpoint
10. `frontend/src/pages/` — all pages from Section 8
11. Run `seed.json` through POST endpoints to populate the DB