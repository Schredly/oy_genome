from typing import Dict, List
from .services.logic import validate_rental_duration
from .services.workflows import approve_or_reject_rental_request

# Function Registry
FUNCTIONS = {
    'validate_rental_duration': validate_rental_duration,
    'approve_or_reject_rental_request': approve_or_reject_rental_request,
}

# Task Router
async def route_task(task_name: str, payload: dict) -> dict:
    fn = FUNCTIONS.get(task_name)
    if not fn:
        return {'error': f'Unknown task: {task_name}'}
    return await fn(**payload)

# Simple Memory
TASK_HISTORY: List[dict] = []

def log_task(task_name: str, payload: dict, result: dict):
    TASK_HISTORY.append({
        'task_name': task_name,
        'payload': payload,
        'result': result,
    })

def get_history(limit: int = 10) -> List[dict]:
    return TASK_HISTORY[-limit:]

# Workflow Executor
WORKFLOWS = {
    'beach_rental_approval': [
        {'action': 'validate_rental_duration'},
        {'action': 'approve_or_reject_rental_request'}
    ]
}

async def execute_workflow(workflow_name: str, context: dict) -> dict:
    steps = WORKFLOWS.get(workflow_name)
    if not steps:
        return {'error': f'Unknown workflow: {workflow_name}'}
    for step in steps:
        result = await route_task(step['action'], context)
        log_task(step['action'], context, result)
        context.update(result)
    return context