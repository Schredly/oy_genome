from fastapi import HTTPException
from ..store import get_beach_rental_by_id, update_beach_rental
from .logic import validate_rental_duration, approve_or_reject_rental

WORKFLOWS = {
    "beach_rental_approval": [
        {"action": "validate_rental_duration"},
        {"action": "approve_or_reject_rental"}
    ]
}

async def execute_workflow(workflow_name: str, rental_id: str) -> dict:
    if workflow_name not in WORKFLOWS:
        raise HTTPException(status_code=404, detail="Workflow not found")
    
    steps = WORKFLOWS[workflow_name]
    context = {"rental_id": rental_id}
    
    for step in steps:
        action = step.get("action")
        if action == "validate_rental_duration":
            await validate_rental_duration(rental_id)
        elif action == "approve_or_reject_rental":
            result = await approve_or_reject_rental(rental_id)
            context.update(result)
        else:
            raise HTTPException(status_code=400, detail=f"Unknown action: {action}")
    
    return context