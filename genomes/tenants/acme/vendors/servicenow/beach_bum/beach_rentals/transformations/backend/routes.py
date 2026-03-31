from fastapi import APIRouter
from .models import UpdateSet
from .store import update_set_store

router = APIRouter()

@router.get("/api/update_set")
async def list_update_sets():
    return update_set_store.list_all()

@router.get("/api/update_set/{id}")
async def get_update_set(id: str):
    return update_set_store.get_by_id(id)

@router.post("/api/update_set")
async def create_update_set(update_set: UpdateSet):
    update_set_store.create(update_set.dict())
    return {"status": "created"}

@router.put("/api/update_set/{id}")
async def update_update_set(id: str, update_set: UpdateSet):
    update_set_store.update(id, update_set.dict())
    return {"status": "updated"}

@router.delete("/api/update_set/{id}")
async def delete_update_set(id: str):
    update_set_store.delete(id)
    return {"status": "deleted"}