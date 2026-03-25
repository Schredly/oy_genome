async def execute_rental_process(customer_name: str, equipment_name: str, duration: int):
    await decrement_inventory(equipment_name, 1)
    return {"message": "Rental process executed"}