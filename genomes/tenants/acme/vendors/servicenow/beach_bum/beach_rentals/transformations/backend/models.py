from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UpdateSet(BaseModel):
    sys_id: str
    sys_created_by: str
    sys_created_on: datetime
    sys_updated_by: str
    sys_updated_on: datetime
    name: str
    state: str

    class Config:
        orm_mode = True