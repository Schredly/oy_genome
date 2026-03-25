from pydantic import BaseModel

class BeachEquipment(BaseModel):
    name: str
    available_quantity: int
    condition: str
    daily_rate: float