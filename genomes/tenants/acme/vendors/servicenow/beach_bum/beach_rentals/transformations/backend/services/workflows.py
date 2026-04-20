from ..store import BeachRentalStore
from .logic import check_customer_eligibility

store = BeachRentalStore()

async def check_customer_eligibility_for_workflow(customer_name: str) -> bool:
    return check_customer_eligibility(customer_name)

async def approve_or_reject_rental_request(rental_id: str) -> dict:
    rental = store.get_by_id(rental_id)
    if not rental:
        return {"status": "error", "message": "Rental not found"}

    eligible = await check_customer_eligibility_for_workflow(rental.customer_name)
    if eligible:
        # Logic to approve the rental request
        return {"status": "approved", "message": f"Rental {rental_id} approved"}
    else:
        # Logic to reject the rental request
        return {"status": "rejected", "message": f"Rental {rental_id} rejected: customer not eligible"}