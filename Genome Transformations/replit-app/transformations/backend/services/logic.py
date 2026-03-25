async def decrement_inventory(item_id: str, quantity: int):
    item = EquipmentStore.get_by_id(item_id)
    if item:
        item['available_quantity'] -= quantity
        EquipmentStore.update(item_id, item)