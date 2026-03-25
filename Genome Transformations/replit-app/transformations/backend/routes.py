from fastapi import APIRouter, HTTPException
from .models import BeachEquipment
from .store import EquipmentStore

router = APIRouter()

@router.get("/api/equipment")
async def list_equipment():
    return EquipmentStore.list_all()

@router.get("/api/equipment/{equipment_id}")
async def get_equipment(equipment_id: str):
    equipment = EquipmentStore.get_by_id(equipment_id)
    if equipment is None:
        raise HTTPException(status_code=404, detail="Equipment not found")
    return equipment

@router.post("/api/equipment")
async def create_equipment(equipment: BeachEquipment):
    EquipmentStore.create(equipment)
    return equipment

@router.put("/api/equipment/{equipment_id}")
async def update_equipment(equipment_id: str, equipment: BeachEquipment):
    EquipmentStore.update(equipment_id, equipment)
    return equipment

@router.delete("/api/equipment/{equipment_id}")
async def delete_equipment(equipment_id: str):
    EquipmentStore.delete(equipment_id)
    return {"detail": "Equipment deleted"}