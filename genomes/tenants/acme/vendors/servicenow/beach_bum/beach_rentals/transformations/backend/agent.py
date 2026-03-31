from fastapi import APIRouter
from .services.logic import transition_update_set_state
from .services.workflows import execute_update_set_management

FUNCTIONS = {
    'transition_update_set_state': transition_update_set_state
}

WORKFLOWS = {
    'update_set_management': execute_update_set_management
}

TASK_HISTORY = []

def log_task(task_name, payload, result):
    TASK_HISTORY.append({'task_name': task_name, 'payload': payload, 'result': result})

def get_history(limit=10):
    return TASK_HISTORY[-limit:]

async def route_task(task_name: str, payload: dict) -> dict:
    fn = FUNCTIONS.get(task_name)
    if not fn:
        return {'error': f'Unknown task: {task_name}'}
    result = await fn(**payload)
    log_task(task_name, payload, result)
    return result

async def execute_workflow(workflow_name: str, context: dict) -> dict:
    workflow_fn = WORKFLOWS.get(workflow_name)
    if not workflow_fn:
        return {'error': f'Unknown workflow: {workflow_name}'}
    result = await workflow_fn(**context)
    log_task(workflow_name, context, result)
    return result

agent_router = APIRouter()

@agent_router.post("/api/agent/execute")
async def execute_task(task: str, payload: dict):
    return await route_task(task, payload)

@agent_router.post("/api/agent/workflow")
async def run_workflow(workflow: str, context: dict):
    return await execute_workflow(workflow, context)

@agent_router.get("/api/agent/history")
async def get_task_history():
    return get_history()