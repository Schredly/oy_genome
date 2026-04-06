from typing import Callable, Dict, Any, List
from fastapi import APIRouter, HTTPException
from .services.logic import validate_rental_duration, approve_or_reject_rental
from .services.workflows import execute_workflow

router = APIRouter()

# --- FUNCTION REGISTRY ---
FUNCTIONS: Dict[str, Callable[..., Any]] = {
    "validate_rental_duration": validate_rental_duration,
    "approve_or_reject_rental": approve_or_reject_rental
}

# --- TASK HISTORY MEMORY ---
TASK_HISTORY: List[Dict[str, Any]] = []

def log_task(task_name: str, payload: Dict[str, Any], result: Dict[str, Any]):
    TASK_HISTORY.append({
        "task_name": task_name,
        "payload": payload,
        "result": result
    })

def get_history(limit: int = 10) -> List[Dict[str, Any]]:
    return TASK_HISTORY[-limit:]

# --- TASK ROUTER ---
async def route_task(task_name: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    fn = FUNCTIONS.get(task_name)
    if not fn:
        return {"error": f"Unknown task: {task_name}"}
    result = await fn(**payload)
    log_task(task_name, payload, result)
    return result

# --- API ENDPOINTS ---
@router.post("/api/agent/execute")
async def execute_task(task: str, payload: Dict[str, Any]):
    result = await route_task(task, payload)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@router.post("/api/agent/workflow")
async def execute_agent_workflow(workflow: str, payload: Dict[str, Any]):
    rental_id = payload.get("rental_id")
    if not rental_id:
        raise HTTPException(status_code=400, detail="Rental ID is required for workflow execution")
    result = await execute_workflow(workflow, rental_id)
    return result

@router.get("/api/agent/history")
async def get_task_history(limit: int = 10):
    return get_history(limit)