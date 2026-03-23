# Master Prompt for Replit App Building

Create a Replit application replicating the ServiceNow Technical Catalog for the ACME tenant sourced from ServiceNow.

## UI Details
- The UI should include forms for requesting services including: Server Reboot, Database Restore, Request Knowledge Base, Application Server (Standard), Application Server (Large), Database Server & Oracle License, Email Account (old), and VM Provisioning.

## API Routes
- Implement routes for service request submissions, approvals, and rejections consistent with existing ServiceNow workflows.

## Data Models
- Define models for each catalog item based on fields present in the files structure/application_server_large.yaml and structure/application_server_standard.yaml.

## Workflows
- Implement necessary workflows and approval processes as per workflows section of the genome description.

## Validation Rules
- Include validation for fields like project codes, budget codes, operating systems, and storage requirements.