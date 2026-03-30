# Workflow definitions to chain together business logic operations.
# Define workflows that connect multiple tasks into a single process.

WORKFLOWS = {
    "reboot_and_restore": [
        {"action": "handle_server_reboot", "params": ["server_id", "reason"]},
        {"action": "perform_database_restore", "params": ["database_id", "backup_source", "restore_point"]},
    ],
    "setup_and_rent_equipment": [
        {"action": "setup_application_server", "params": ["server_type", "os", "storage"]},
        {"action": "rent_beach_equipment", "params": ["customer_name", "equipment_type", "quantity"]},
    ],
    "create_kb_and_notify": [
        {"action": "create_knowledge_base", "params": ["request_title", "reason"]},
        # Additional actions like sending notification can be added here
    ]
}

# These workflows demonstrate chaining of tasks. Additional workflows can be added following the same pattern.
# The task router will need to support these workflow executions by extracting parameters and calling functions.