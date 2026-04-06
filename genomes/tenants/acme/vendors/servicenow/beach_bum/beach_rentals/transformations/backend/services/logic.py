from ..store import get_beach_rental_by_id, update_beach_rental
from fastapi import HTTPException

async def validate_rental_duration(rental_id: str):
    beach_rental = get_beach_rental_by_id(rental_id)
    if not beach_rental:
        raise HTTPException(status_code=404, detail="Beach Rental not found")
    
    if beach_rental.u_rental_duration <= 0:
        raise HTTPException(status_code=400, detail="Rental duration must be greater than zero")

    # Add more validation logic if necessary
    return True

async def check_customer_eligibility(customer_name: str) -> bool:
    # Placeholder function to simulate an external check
    # In a real environment, this would likely involve checking an external system.
    return True

async def approve_or_reject_rental(rental_id: str):
    if await validate_rental_duration(rental_id):
        # Assuming a placeholder function for customer eligibility check
        beach_rental = get_beach_rental_by_id(rental_id)
        if beach_rental and await check_customer_eligibility(beach_rental.u_customer_name):
            beach_rental.status = "approved"
            update_beach_rental(rental_id, beach_rental)
            return {"status": "approved"}
        else:
            beach_rental.status = "rejected"
            update_beach_rental(rental_id, beach_rental)
            return {"status": "rejected"}
    return {"status": "validation_failed"}