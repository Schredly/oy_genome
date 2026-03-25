FUNCTIONS = {
    'decrement_inventory': decrement_inventory,
    'execute_rental_process': execute_rental_process
}

async def route_task(task_name: str, payload: dict) -> dict:
    fn = FUNCTIONS.get(task_name)
    if not fn:
        return {'error': f'Unknown task: {task_name}'}
    return await fn(**payload)

TASK_HISTORY = []

async def execute_workflow(workflow_name: str, context: dict) -> dict:
    steps = WORKFLOWS[workflow_name]
    for step in steps:
        result = await route_task(step['action'], context)
        context.update(result)
    return context