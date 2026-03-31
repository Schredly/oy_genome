from ..store import update_set_store

async def transition_update_set_state(sys_id: str, new_state: str):
    update_set = update_set_store.get_by_id(sys_id)
    if update_set:
        update_set['state'] = new_state
        update_set_store.update(sys_id, update_set)
        return {"status": "state updated", "sys_id": sys_id, "new_state": new_state}
    return {"error": "update set not found", "sys_id": sys_id}