from typing import List, Optional
from .models import BeachRental

# In-memory store for simplicity
beach_rental_store: List[BeachRental] = []

def create_beach_rental(beach_rental: BeachRental) -> BeachRental:
    beach_rental.sys_id = str(len(beach_rental_store) + 1)
    beach_rental_store.append(beach_rental)
    return beach_rental

def get_beach_rental_by_id(rental_id: str) -> Optional[BeachRental]:
    for rental in beach_rental_store:
        if rental.sys_id == rental_id:
            return rental
    return None

def list_all_beach_rentals() -> List[BeachRental]:
    return beach_rental_store

def update_beach_rental(rental_id: str, update: BeachRental) -> Optional[BeachRental]:
    for idx, rental in enumerate(beach_rental_store):
        if rental.sys_id == rental_id:
            beach_rental_store[idx] = update
            beach_rental_store[idx].sys_id = rental_id
            return beach_rental_store[idx]
    return None

def delete_beach_rental(rental_id: str) -> bool:
    for idx, rental in enumerate(beach_rental_store):
        if rental.sys_id == rental_id:
            del beach_rental_store[idx]
            return True
    return False