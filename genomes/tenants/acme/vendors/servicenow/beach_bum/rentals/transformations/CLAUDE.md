# Project Overview
The Beach Bum application is designed to manage beach equipment inventory and customer checkouts. It provides features to handle equipment rentals, track inventory, and manage customer interactions.

## Tech Stack
- Python 3.11 + FastAPI + Pydantic v2
- React 19 + TS + Vite + TailwindCSS + shadcn/ui
- SQLite

## Data Models
### Entity: Beach Equipment
- **Table**: x_beachbum_equipment
- **Fields**:
  - available_quantity (integer)
  - condition (string)
  - daily_rate (decimal)

## API Endpoints
### Beach Equipment
- GET /equipment
- POST /equipment
- PUT /equipment/{id}
- DELETE /equipment/{id}

## Business Logic
1. **Reduce Inventory on Checkout**
   - Trigger: before insert on x_beachbum_checkout
   - Logic: Reduces inventory count when a checkout is created.

## Workflows
### Rental Process
- Trigger: Initiate Rental Request
- Steps:
  1. Customer chooses equipment and rental duration
  2. System creates a checkout record
  3. Customer returns equipment

## UI Pages
- Dashboard
- Active Checkouts
- All Checkouts
- Add Equipment Form
- All Equipment List

## Events
- **checkout_created_event**: Triggers inventory decrement logic
- **equipment_returned_event**: Triggers inventory increment logic

## Build Order
1. Set up FastAPI backend
2. Define Pydantic models
3. Add API routing
4. Implement UI with React
5. Seed the database

## Architecture Rules
- Use entity pattern with model, repo, router, and service
- Implement workflows with a WorkflowEngine
- Ensure consistent API response envelopes.