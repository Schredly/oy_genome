# Replit Application Master Prompt

## Overview
Transform the Human Resources Catalog from ServiceNow into a standalone web application using Replit. This application will replicate the functionality of the catalog items, workflows, and data attributes as defined in the ServiceNow genome.

## UI Design
Create user interfaces for various HR processes like Direct Deposit Inquiry, HR Report Inquiry, and more. Each process should have a dedicated page to handle inputs and display information.

## API Routes
- /api/deposit-inquiry: Endpoint for handling Direct Deposit Inquiries.
- /api/report-inquiry: Endpoint for HR Report Inquiries.
- /api/employee-profile-update: Endpoint for updating employee profiles.

## Data Models
- **Direct Deposit Inquiry**: Includes fields like `direct_deposit_current`, `deposit_type`, `deposit_percent`, and more.
- **HR Report Inquiry**: Includes fields such as `hr_system`.

## Workflows
Implement the following key workflows:
- `direct_deposit_inquiry_request`
- `hr_report_inquiry_request`
- Approval workflows as needed for sensitive processes like Erasure of Personal Data.

## Validation Rules
Ensure all fields comply with validation rules from the YAML descriptions, e.g., mandatory checks and input formats.