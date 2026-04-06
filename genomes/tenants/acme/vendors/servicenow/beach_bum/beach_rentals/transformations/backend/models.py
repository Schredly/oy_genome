from pydantic import BaseModel
from typing import Optional, List

class BeachRental(BaseModel):
    u_rental_duration: int
    u_customer_name: str
    u_rental_type: str
    sys_id: Optional[str] = None
    created_on: Optional[str] = None
    created_by: Optional[str] = None
    updated_on: Optional[str] = None
    updated_by: Optional[str] = None

class RentalRequest(BaseModel):
    rental_duration: int
    customer_name: str
    rental_type: str

class WorkflowStep(BaseModel):
    step: int
    actor: str
    action: str
    system_behavior: str

class EquipmentRentalProcess(BaseModel):
    name: str
    steps: List[WorkflowStep]

class BusinessLogicRule(BaseModel):
    name: str
    table: str
    trigger: str
    logic_summary: str
    external_dependencies: Optional[str] = None