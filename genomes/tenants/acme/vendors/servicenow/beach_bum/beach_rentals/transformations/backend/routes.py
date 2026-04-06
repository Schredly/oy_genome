from fastapi import APIRouter, HTTPException
from typing import List
from .store import (
    create_beach_rental,
    get_beach_rental_by_id,
    list_all_beach_rentals,
    update_beach_rental,
    delete_beach_rental,
)
from .models import BeachRental

router = APIRouter()

@router.get("/api/beach_rentals", response_model=List[BeachRental])
async def get_beach_rentals():
    return list_all_beach_rentals()

@router.get("/api/beach_rentals/{rental_id}", response_model=BeachRental)
async def get_beach_rental(rental_id: str):
    beach_rental = get_beach_rental_by_id(rental_id)
    if not beach_rental:
        raise HTTPException(status_code=404, detail="Beach Rental not found")
    return beach_rental

@router.post("/api/beach_rentals", response_model=BeachRental)
async def post_beach_rental(beach_rental: BeachRental):
    return create_beach_rental(beach_rental)

@router.put("/api/beach_rentals/{rental_id}", response_model=BeachRental)
async def put_beach_rental(rental_id: str, beach_rental: BeachRental):
    updated_rental = update_beach_rental(rental_id, beach_rental)
    if not updated_rental:
        raise HTTPException(status_code=404, detail="Beach Rental not found for update")
    return updated_rental

@router.delete("/api/beach_rentals/{rental_id}")
async def delete_beach_rental_endpoint(rental_id: str):
    success = delete_beach_rental(rental_id)
    if not success:
        raise HTTPException(status_code=404, detail="Beach Rental not found for deletion")
    return {"detail": "Beach Rental deleted successfully"}