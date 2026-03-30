from pydantic import BaseModel, Field
from typing import Optional

# Pydantic models for each entity

class ServerReboot(BaseModel):
    server_details: Optional[str] = Field(default=None)
    cmdb_ci: str
    reboot_date: Optional[str] = Field(default=None)
    reason: Optional[str] = Field(default=None)
    reason_details: Optional[str] = Field(default=None)

class DatabaseRestore(BaseModel):
    cmdb_ci: str
    con: Optional[str] = Field(default=None)
    backup_source: Optional[str] = Field(default=None)
    restore_pit: Optional[str] = Field(default=None)
    reason: Optional[str] = Field(default=None)
    reason_details: Optional[str] = Field(default=None)

class BeachEquipmentRental(BaseModel):
    customer_name: str
    customer_phone: str
    customer_email: Optional[str] = Field(default=None)
    rental_date: str
    equipment_type: str
    quantity: str
    rental_duration: str
    return_date: str
    special_requests: Optional[str] = Field(default=None)

class RequestKnowledgeBase(BaseModel):
    request_reason: Optional[str] = Field(default=None)
    requested_title: Optional[str] = Field(default=None)

class ApplicationServerStandard(BaseModel):
    project_code: Optional[str] = Field(default=None)
    budget_code: Optional[str] = Field(default=None)
    OS: Optional[str] = Field(default=None)
    san: Optional[str] = Field(default=None)

class ApplicationServerLarge(BaseModel):
    project_code: Optional[str] = Field(default=None)
    budget_code: Optional[str] = Field(default=None)
    OS: Optional[str] = Field(default=None)
    san: Optional[str] = Field(default=None)

class DatabaseServerOracleLicense(BaseModel):
    project_code: Optional[str] = Field(default=None)
    budget_code: Optional[str] = Field(default=None)
    OS: Optional[str] = Field(default=None)
    san: Optional[str] = Field(default=None)

class EmailAccountOld(BaseModel):
    is_this_a_new_account: Optional[str] = Field(default=None)
    special_requirements: Optional[str] = Field(default=None)