## Replit Application Master Prompt

### Application Overview
Create a standalone web application based on the ServiceNow Technical Catalog.

#### UI
Design a responsive user interface that allows users to interact with...

#### API Routes
- `/server_reboot_request`: Trigger a workflow to request a server reboot.
- `/database_restore_request`: Initiate a request for database restoration.

#### Data Models
Use structures from the provided genome, such as `Server Reboot`, `Database Restore`, etc.

#### Workflows
- `server_reboot_request`: Guide the user to fill the necessary details for a server reboot.
- `database_restore_request`: Capture specifics like restore time and additional approvals.

### Validation Rules
Ensure all required fields are checked before submission.

### Approval Workflows
Reflect the existing ServiceNow workflows within the new application...