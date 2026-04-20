from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from .store import BeachRentalStore
from .models import BeachRental, BeachRentalCreate, BeachRentalUpdate

router = APIRouter()

class BeachRentalCreateRequest(BaseModel):
    rental_duration: int
    customer_name: str
    rental_type: str

class BeachRentalUpdateRequest(BaseModel):
    rental_duration: int
    rental_type: str

# Simulated database / store
beach_rental_store = BeachRentalStore()

@router.get("/api/beach_rentals", response_model=List[BeachRental])
async def list_beach_rentals():
    return beach_rental_store.list_all()

@router.get("/api/beach_rentals/{rental_id}", response_model=BeachRental)
async def get_beach_rental(rental_id: str):
    rental = beach_rental_store.get_by_id(rental_id)
    if rental is None:
        raise HTTPException(status_code=404, detail="Beach Rental not found")
    return rental

@router.post("/api/beach_rentals", response_model=BeachRental)
async def create_beach_rental(rental: BeachRentalCreateRequest):
    new_rental = BeachRentalCreate(
        rental_duration=rental.rental_duration,
        customer_name=rental.customer_name,
        rental_type=rental.rental_type
    )
    return beach_rental_store.create(new_rental)

@router.put("/api/beach_rentals/{rental_id}", response_model=BeachRental)
async def update_beach_rental(rental_id: str, rental: BeachRentalUpdateRequest):
    if not beach_rental_store.exists(rental_id):
        raise HTTPException(status_code=404, detail="Beach Rental not found")
    updated_rental = BeachRentalUpdate(
        rental_duration=rental.rental_duration,
        rental_type=rental.rental_type
    )
    return beach_rental_store.update(rental_id, updated_rental)

@router.delete("/api/beach_rentals/{rental_id}", response_model=dict)
async def delete_beach_rental(rental_id: str):
    if not beach_rental_store.exists(rental_id):
        raise HTTPException(status_code=404, detail="Beach Rental not found")
    beach_rental_store.delete(rental_id)
    return {"status": "deleted"}