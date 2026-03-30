from typing import Dict, Callable, Any, List
from .services.logic import handle_server_reboot, perform_database_restore, rent_beach_equipment, create_knowledge_base, setup_application_server
from .services.workflows import WORKFLOWS

# Function registry for business logic
FUNCTIONS: Dict[str, Callable] = {
    "handle_server_reboot": handle_server_reboot,
    "perform_database_restore": perform_database_restore,
    "rent_beach_equipment": rent_beach_equipment,
    "create_knowledge_base": create_knowledge_base,
    "setup_application_server": setup_application_server
}

# Simple task execution history
TASK_HISTORY: List[Dict] = []

def log_task(task_name: str, payload: Dict, result: Dict):
    TASK_HISTORY.append({
        "task": task_name,
        "payload": payload,
        "result": result
    })

def get_history(limit: int = 10) -> List[Dict]:
    return TASK_HISTORY[-limit:]

async def route_task(task_name: str, payload: Dict) -> Dict:
    fn = FUNCTIONS.get(task_name)
    if not fn:
        return {'error': f'Unknown task: {task_name}'}
    result = await fn(**payload)
    log_task(task_name, payload, result)
    return result

async def execute_workflow(workflow_name: str, context: Dict) -> Dict:
    steps = WORKFLOWS.get(workflow_name)
    if not steps:
        return {'error': f'Unknown workflow: {workflow_name}'}
    for step in steps:
        action = step['action']
        params = {key: context.get(key) for key in step['params']}
        result = await route_task(action, params)
        context.update(result)
    return context

def retrieve(query: str, collection: str) -> List[Dict]:
    # Placeholder for retrieval logic, e.g., searching in-memory store by keyword
    # This is a stub implementation and needs to be developed based on actual requirements
    return []