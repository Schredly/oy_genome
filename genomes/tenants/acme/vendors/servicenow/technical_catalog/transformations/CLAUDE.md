# CLAUDE.md

## Section 1: Project Overview

**Application Name:** Technical Catalog

**Description:** This application is designed to manage various IT services offered by the organization. It allows users to request services such as server reboots, database restores, beach equipment rentals, application servers, and more.

**Entities:**
- Server Reboot
- Database Restore
- Beach Equipment Rental
- Request Knowledge Base
- Application Server (Standard)
- Application Server (Large)
- Database Server & Oracle License
- Email Account (old)
- VM Provisioning

**Workflows:**
- Server Reboot request
- Database Restore request
- Beach Equipment Rental request
- Request Knowledge Base request
- Application Server (Standard) request
- Application Server (Large) request
- Database Server & Oracle License request
- Email Account (old) request
- VM Provisioning request

## Section 2: Tech Stack

**Backend:** Python 3.11, FastAPI, Pydantic v2, SQLAlchemy 2.0, SQLite  
**Frontend:** React 19, TypeScript, Vite, TailwindCSS, shadcn/ui

## Section 3: Data Models

### Server Reboot

```python
from enum import Enum
from pydantic import BaseModel
from datetime import datetime
from sqlmodel import SQLModel, Field

class ServerRebootStatus(str, Enum):
    pending = 'pending'
    completed = 'completed'

class ServerReboot(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    cmdb_ci: str
    reboot_date: datetime
    reason: str
    reason_details: str | None = None
    status: ServerRebootStatus = ServerRebootStatus.pending

class ServerRebootCreate(BaseModel):
    cmdb_ci: str
    reboot_date: datetime
    reason: str
    reason_details: str | None = None

class ServerRebootUpdate(BaseModel):
    reboot_date: datetime | None = None
    reason: str | None = None
    status: ServerRebootStatus | None = None
```

### Database Restore

```python
class DatabaseRestore(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    cmdb_ci: str
    backup_source: str | None = None
    restore_pit: datetime | None = None
    reason: str
    reason_details: str | None = None

class DatabaseRestoreCreate(BaseModel):
    cmdb_ci: str
    backup_source: str | None = None
    restore_pit: datetime | None = None
    reason: str
    reason_details: str | None = None

class DatabaseRestoreUpdate(BaseModel):
    backup_source: str | None = None
    restore_pit: datetime | None = None
    reason: str | None = None
```

### Beach Equipment Rental

```python
class EquipmentType(str, Enum):
    chair = 'chair'
    umbrella = 'umbrella'
    surfboard = 'surfboard'
    boogie_board = 'boogie_board'
    towel = 'towel'

class BeachEquipmentRental(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    customer_name: str
    customer_phone: str
    customer_email: str
    rental_date: datetime
    equipment_type: EquipmentType
    quantity: int
    rental_duration: int  # in days
    return_date: datetime
    special_requests: str | None = None

class BeachEquipmentRentalCreate(BaseModel):
    customer_name: str
    customer_phone: str
    customer_email: str
    rental_date: datetime
    equipment_type: EquipmentType
    quantity: int
    rental_duration: int
    special_requests: str | None = None

class BeachEquipmentRentalUpdate(BaseModel):
    rental_date: datetime | None = None
    equipment_type: EquipmentType | None = None
    quantity: int | None = None
    rental_duration: int | None = None
    special_requests: str | None = None
```

### Request Knowledge Base

```python
class RequestKnowledgeBase(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    request_reason: str
    requested_title: str

class RequestKnowledgeBaseCreate(BaseModel):
    request_reason: str
    requested_title: str

class RequestKnowledgeBaseUpdate(BaseModel):
    request_reason: str | None = None
    requested_title: str | None = None
```

### Application Server (Standard)

```python
class ApplicationServerStandard(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    project_code: str
    budget_code: str
    OS: str  # Operating System
    san: int | None = None  # SAN Storage in GB

class ApplicationServerStandardCreate(BaseModel):
    project_code: str
    budget_code: str
    OS: str
    san: int | None = None

class ApplicationServerStandardUpdate(BaseModel):
    OS: str | None = None
    san: int | None = None
```

### Application Server (Large)

```python
class ApplicationServerLarge(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    project_code: str
    budget_code: str
    OS: str
    san: int | None = None

class ApplicationServerLargeCreate(BaseModel):
    project_code: str
    budget_code: str
    OS: str
    san: int | None = None

class ApplicationServerLargeUpdate(BaseModel):
    OS: str | None = None
    san: int | None = None
```

### Database Server & Oracle License

```python
class DatabaseServerOracleLicense(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    project_code: str
    budget_code: str
    OS: str
    san: int | None = None

class DatabaseServerOracleLicenseCreate(BaseModel):
    project_code: str
    budget_code: str
    OS: str
    san: int | None = None

class DatabaseServerOracleLicenseUpdate(BaseModel):
    OS: str | None = None
    san: int | None = None
```

### Email Account (old)

```python
class EmailAccountOld(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    is_this_a_new_account: bool
    special_requirements: str | None = None

class EmailAccountOldCreate(BaseModel):
    is_this_a_new_account: bool
    special_requirements: str | None = None

class EmailAccountOldUpdate(BaseModel):
    special_requirements: str | None = None
```

### VM Provisioning

```python
class VMProvisioning(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    cpu: int
    ram: int  # in GB
    storage: int  # in GB

class VMProvisioningCreate(BaseModel):
    cpu: int
    ram: int
    storage: int

class VMProvisioningUpdate(BaseModel):
    cpu: int | None = None
    ram: int | None = None
    storage: int | None = None
```

## Section 4: API Endpoints

### Server Reboot

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()

@router.get('/server_reboots', response_model=list[ServerReboot])
async def list_server_reboots(db: Session = Depends(get_db)):
    ...

@router.post('/server_reboots', response_model=ServerReboot)
async def create_server_reboot(body: ServerRebootCreate, db: Session = Depends(get_db)):
    ...

@router.put('/server_reboots/{id}', response_model=ServerReboot)
async def update_server_reboot(id: int, body: ServerRebootUpdate, db: Session = Depends(get_db)):
    ...
```

### Database Restore

```python
@router.get('/database_restores', response_model=list[DatabaseRestore])
async def list_database_restores(db: Session = Depends(get_db)):
    ...

@router.post('/database_restores', response_model=DatabaseRestore)
async def create_database_restore(body: DatabaseRestoreCreate, db: Session = Depends(get_db)):
    ...

@router.put('/database_restores/{id}', response_model=DatabaseRestore)
async def update_database_restore(id: int, body: DatabaseRestoreUpdate, db: Session = Depends(get_db)):
    ...
```

### Beach Equipment Rental

```python
@router.get('/beach_equipment_rentals', response_model=list[BeachEquipmentRental])
async def list_beach_equipment_rentals(db: Session = Depends(get_db)):
    ...

@router.post('/beach_equipment_rentals', response_model=BeachEquipmentRental)
async def create_beach_equipment_rental(body: BeachEquipmentRentalCreate, db: Session = Depends(get_db)):
    ...

@router.put('/beach_equipment_rentals/{id}', response_model=BeachEquipmentRental)
async def update_beach_equipment_rental(id: int, body: BeachEquipmentRentalUpdate, db: Session = Depends(get_db)):
    ...
```

### Request Knowledge Base

```python
@router.get('/request_knowledge_bases', response_model=list[RequestKnowledgeBase])
async def list_request_knowledge_bases(db: Session = Depends(get_db)):
    ...

@router.post('/request_knowledge_bases', response_model=RequestKnowledgeBase)
async def create_request_knowledge_base(body: RequestKnowledgeBaseCreate, db: Session = Depends(get_db)):
    ...

@router.put('/request_knowledge_bases/{id}', response_model=RequestKnowledgeBase)
async def update_request_knowledge_base(id: int, body: RequestKnowledgeBaseUpdate, db: Session = Depends(get_db)):
    ...
```

## Section 5: Business Logic

### Server Reboot Logic

```python
async def reboot_server(db: Session, server_id: int):
    '''Initiates a server reboot process for the given server_id.'''
    ...

### Database Restore Logic

```python
async def restore_database(db: Session, database_id: int, backup_source: str):
    '''Restores a database from the specified backup source.'''
    ...

### Beach Equipment Rental Logic

```python
async def process_rental(db: Session, rental_id: int):
    '''Processes a new rental request, updating inventory and reservations.'''
    ...

## Section 6: Workflows

```python
RENTAL_WORKFLOW = [
    Step('request', actor='customer', action='submit_rental_form', calls=['process_rental']),
    Step('approve', actor='manager', action='review_rental_request', calls=['approve_rental']),
    Step('issue', actor='staff', action='issue_equipment', calls=['update_inventory']),
]
```

## Section 7: Event Handlers

```python
@on_event('rental_created')
async def on_rental_created(rental: BeachEquipmentRental, db: Session):
    await process_rental(db, rental.id)
    ...
```

## Section 8: UI Pages

**Rental Request Form**
- **Route:** `/rental-request`
- **Component:** `RentalRequestPage`
- **Data Source:** `/api/beach_equipment_rentals`
- **Key Features:** Form for submitting new rentals, includes customer info and equipment selection fields.

**Server Reboot Request**
- **Route:** `/server-reboot`
- **Component:** `ServerRebootPage`
- **Data Source:** `/api/server_reboots`
- **Key Features:** Form to submit server reboot requests and specify reboot details.

## Section 9: Navigation

- **Dashboard:** `/dashboard` | Icon: `home`
- **Beach Equipment Rental:** `/rental-request` | Icon: `beach_access`
- **Server Reboot:** `/server-reboot` | Icon: `replay`
- **Knowledge Base Request:** `/knowledge-base-request` | Icon: `book`

## Section 10: Architecture Rules

- **Entity pattern:** models.py → database.py → services/\{name\}.py → routers/\{name\}.py
- **All routes:** return \{status, data\} envelope
- **Business logic:** lives in services/, never in routers
- **DB session:** via FastAPI Depends(get_db)

## Section 11: Build Order

1. **Scaffold:** Create backend/ and frontend/ with venv + package.json
2. **Models:** backend/models.py — all Pydantic models and enums from Section 3
3. **Database:** backend/database.py — SQLAlchemy engine + Base + get_db + create_tables()
4. **Services:** backend/services/\{entity\}.py — all service functions from Section 5
5. **Workflows:** backend/workflows.py — Step dataclass + workflow definitions from Section 6
6. **Events:** backend/events.py — event bus + handlers from Section 7
7. **Routers:** backend/routers/\{entity\}.py — all FastAPI routes from Section 4
8. **Main App:** backend/main.py — app factory, CORS, lifespan (create_tables), router includes
9. **Frontend API:** frontend/src/api/ — typed fetch hooks for each endpoint
10. **Pages:** frontend/src/pages/ — all pages from Section 8
11. **Seed DB:** Run seed.json through POST endpoints to populate the DB