from ..store import BeachRentalStore

store = BeachRentalStore()

async def validate_rental_duration(rental_duration: int, customer_name: str) -> bool:
    if rental_duration <= 0:
        return False
    
    # Example validation logic, assuming a method to check customer eligibility
    customer_eligible = check_customer_eligibility(customer_name)
    if not customer_eligible:
        return False

    return True

def check_customer_eligibility(customer_name: str) -> bool:
    # Simulate checking an external database for customer eligibility
    # In a real scenario, this would involve an API call or database query
    eligible_customers = ["Jane Doe", "John Smith", "Alice Johnson"]
    return customer_name in eligible_customers