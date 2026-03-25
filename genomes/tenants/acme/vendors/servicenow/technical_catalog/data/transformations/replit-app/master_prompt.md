# Master Prompt

## Overview
You are building a Replit application to simulate a technical catalog service from ServiceNow. The application includes various service catalog items, each with specific workflows and data models.

## UI Design
1. **Homepage**: Display all catalog items with brief descriptions.
2. **Request Form Page**: Dynamic forms based on selected catalog items with fields from the technical catalog YAML data.
3. **Workflows Dashboard**: Show active workflows, with options for user interaction based on the genome's workflow list.

## API Routes
- **GET /catalog-items**: Retrieve all catalog items.
- **POST /catalog-items/:id/request**: Submit a request for a specific catalog item.
- **GET /workflows**: Fetch ongoing workflows.

## Data Models
- **CatalogItem**: Reflects items in the catalog with fields like 'name', 'description', 'sys_id'.
- **Variable**: Represents fields in forms, from 'variables' key in genome.yaml with types and mandatory flags.

## Workflows
Incorporate key workflows identified in genome.yaml like 'Send Notification', 'Update Request'. These should influence UI behavior and API responses appropriately, offering support for approval or task-related functions.

## Special Features
- **Validation**: Enforce mandatory fields as noted in the YAML structure.
- **Approval Processes**: Simulate approval stages using the workflow descriptions and data.