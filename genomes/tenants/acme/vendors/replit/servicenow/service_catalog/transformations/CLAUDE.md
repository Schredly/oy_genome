# Section 1: Project Overview

The application, Service Catalog, is a comprehensive IT Service Management tool that allows users to request various IT services like application server provisioning, database management, VM provisioning, and more. It features a structured process for service request submission and approval and facilitates clear communication between IT staff and users through a user-friendly interface. 

**Entities:**
- Service

**Workflows:**
- Service Request

# Section 2: Tech Stack

**Backend:** Python 3.11, FastAPI, Pydantic v2, SQLAlchemy 2.0, SQLite

**Frontend:** React 19, TypeScript, Vite, TailwindCSS, shadcn/ui

# Section 3: Data Models — WRITE ACTUAL PYTHON CODE

For the table identified, we will create the following models. 

### Status Enum
```python
from enum import Enum

class Status(str, Enum):
    AVAILABLE = 'available'
    UNAVAILABLE = 'unavailable'
```

### Service SQLAlchemy Model
```python
from sqlalchemy import Column, Integer, String, Enum as SQLAEnum, create_engine, Base

class Service(Base):
    __tablename__ = 'services'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    service_name = Column(String, nullable=False)
    description = Column(String)
    category = Column(String, nullable=False)
    status = Column(SQLAEnum(Status), nullable=False)
```

### Service Pydantic Models
```python
from pydantic import BaseModel

class ServiceBase(BaseModel):
    service_name: str
    description: str | None
    category: str
    status: Status

class ServiceCreate(ServiceBase):
    ...

class ServiceUpdate(ServiceBase):
    ...

class ServiceInDB(ServiceBase):
    id: int
```

# Section 4: API Endpoints — WRITE ACTUAL FASTAPI SIGNATURES

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()

@router.get('/services', response_model=list[ServiceInDB])
async def list_services(category: str | None = None, db: Session = Depends(get_db)):
    ...

@router.post('/services', response_model=ServiceInDB)
async def create_service(service: ServiceCreate, db: Session = Depends(get_db)):
    ...

@router.put('/services/{service_id}', response_model=ServiceInDB)
async def update_service(service_id: int, service: ServiceUpdate, db: Session = Depends(get_db)):
    ...

@router.get('/services/{service_id}', response_model=ServiceInDB)
async def get_service(service_id: int, db: Session = Depends(get_db)):
    ...
```

# Section 5: Business Logic — WRITE ACTUAL FUNCTION SIGNATURES

```python
async def validate_service_availability(service: Service, db: Session) -> bool:
    ''' Validates if a service is available for provisioning '''
    ...

async def process_service_request(service: Service, db: Session) -> Service:
    ''' Process the service provisioning workflow steps '''
    ...
```

# Section 6: Workflows

```python
from workflows import Step

SERVICE_REQUEST_WORKFLOW = [
    Step('select_service', actor='user', action='select_service', emits='service_selected'),
    Step('provide_details', actor='user', action='fill_service_details'),
    Step('submit_request', actor='user', action='submit_service_request', emits='request_submitted'),
    Step('approval', actor='admin', action='approve_service_request', emits='request_approved'),
    Step('provisioning', actor='system', action='provision_service', emits='service_provisioned'),
    Step('complete', actor='system', action='finalize_request', emits='service_completed'),
]
```

# Section 7: Event Handlers

```python
@on_event('request_submitted')
async def on_request_submitted(service_id: int, db: Session):
    service = await get_service_by_id(service_id, db)
    if not validate_service_availability(service, db):
        raise HTTPException(status_code=400, detail="Service not available")
    ...

@on_event('service_provisioned')
async def on_service_provisioned(service_id: int, db: Session):
    ...
```

# Section 8: UI Pages

**Routes:**
- `service-catalog/all`: Display list of all services
- `service-catalog/help-you`: Form to request help
- `service-catalog/emergency-changes`: Emergency service requests
- `service-catalog/infrastructure`: Infrastructure services
- `service-catalog/services`: Detailed view of services

**RentalRequestForm fields:**
- `service_name`: TextInput, required
- `description`: Textarea, optional
- `category`: Select (Application Server, Database, VM Provisioning, Email Account), required
- `status`: TextInput, required

# Section 9: Navigation

- **Technical Catalog**
  - **All**
  - **Can We Help You?**
  - **Emergency Changes**
  - **Infrastructure**
  - **Services**

# Section 10: Architecture Rules

- Entity pattern: models.py → database.py → services/{name}.py → routers/{name}.py
- All routes return {status, data} envelope
- Business logic lives in services/, never in routers
- DB session via FastAPI Depends(get_db)

# Section 11: Build Order

1. Scaffold: create backend/ and frontend/ with venv + package.json
2. `backend/models.py` — all Pydantic models and enums from Section 3
3. `backend/database.py` — SQLAlchemy engine + Base + get_db + create_tables()
4. `backend/services/services.py` — all service functions from Section 5
5. `backend/workflows.py` — Step dataclass + workflow definitions from Section 6
6. `backend/events.py` — event bus + handlers from Section 7
7. `backend/routers/services.py` — all FastAPI routes from Section 4
8. `backend/main.py` — app factory, CORS, lifespan (create_tables), router includes
9. `frontend/src/api/` — typed fetch hooks for each endpoint
10. `frontend/src/pages/` — all pages from Section 8
11. Run seed.json through POST endpoints to populate the DB