from fastapi import APIRouter, HTTPException
from .store import Store
from .models import ServerReboot, DatabaseRestore, BeachEquipmentRental, RequestKnowledgeBase, ApplicationServerStandard, ApplicationServerLarge, DatabaseServerOracleLicense, EmailAccountOld

router = APIRouter()
store = Store()

# Server Reboot Endpoints
@router.get("/server-reboot", response_model=list[ServerReboot])
async def list_server_reboots():
    return store.list_all('server_reboot')

@router.post("/server-reboot", response_model=ServerReboot)
async def create_server_reboot(item: ServerReboot):
    return store.create('server_reboot', item)

@router.get("/server-reboot/{item_id}", response_model=ServerReboot)
async def get_server_reboot(item_id: str):
    item = store.get_by_id('server_reboot', item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Server Reboot not found")
    return item

@router.put("/server-reboot/{item_id}", response_model=ServerReboot)
async def update_server_reboot(item_id: str, item: ServerReboot):
    return store.update('server_reboot', item_id, item)

@router.delete("/server-reboot/{item_id}")
async def delete_server_reboot(item_id: str):
    success = store.delete('server_reboot', item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Server Reboot not found")
    return {"detail": "Server Reboot deleted"}

# Repeat similar CRUD endpoints for each entity
# Database Restore Endpoints
@router.get("/database-restore", response_model=list[DatabaseRestore])
async def list_database_restores():
    return store.list_all('database_restore')

@router.post("/database-restore", response_model=DatabaseRestore)
async def create_database_restore(item: DatabaseRestore):
    return store.create('database_restore', item)

@router.get("/database-restore/{item_id}", response_model=DatabaseRestore)
async def get_database_restore(item_id: str):
    item = store.get_by_id('database_restore', item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Database Restore not found")
    return item

@router.put("/database-restore/{item_id}", response_model=DatabaseRestore)
async def update_database_restore(item_id: str, item: DatabaseRestore):
    return store.update('database_restore', item_id, item)

@router.delete("/database-restore/{item_id}")
async def delete_database_restore(item_id: str):
    success = store.delete('database_restore', item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Database Restore not found")
    return {"detail": "Database Restore deleted"}

# Beach Equipment Rental Endpoints
@router.get("/beach-equipment-rental", response_model=list[BeachEquipmentRental])
async def list_beach_equipment_rentals():
    return store.list_all('beach_equipment_rental')

@router.post("/beach-equipment-rental", response_model=BeachEquipmentRental)
async def create_beach_equipment_rental(item: BeachEquipmentRental):
    return store.create('beach_equipment_rental', item)

@router.get("/beach-equipment-rental/{item_id}", response_model=BeachEquipmentRental)
async def get_beach_equipment_rental(item_id: str):
    item = store.get_by_id('beach_equipment_rental', item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Beach Equipment Rental not found")
    return item

@router.put("/beach-equipment-rental/{item_id}", response_model=BeachEquipmentRental)
async def update_beach_equipment_rental(item_id: str, item: BeachEquipmentRental):
    return store.update('beach_equipment_rental', item_id, item)

@router.delete("/beach-equipment-rental/{item_id}")
async def delete_beach_equipment_rental(item_id: str):
    success = store.delete('beach_equipment_rental', item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Beach Equipment Rental not found")
    return {"detail": "Beach Equipment Rental deleted"}

# Request Knowledge Base Endpoints
@router.get("/request-knowledge-base", response_model=list[RequestKnowledgeBase])
async def list_request_knowledge_bases():
    return store.list_all('request_knowledge_base')

@router.post("/request-knowledge-base", response_model=RequestKnowledgeBase)
async def create_request_knowledge_base(item: RequestKnowledgeBase):
    return store.create('request_knowledge_base', item)

@router.get("/request-knowledge-base/{item_id}", response_model=RequestKnowledgeBase)
async def get_request_knowledge_base(item_id: str):
    item = store.get_by_id('request_knowledge_base', item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Knowledge Base Request not found")
    return item

@router.put("/request-knowledge-base/{item_id}", response_model=RequestKnowledgeBase)
async def update_request_knowledge_base(item_id: str, item: RequestKnowledgeBase):
    return store.update('request_knowledge_base', item_id, item)

@router.delete("/request-knowledge-base/{item_id}")
async def delete_request_knowledge_base(item_id: str):
    success = store.delete('request_knowledge_base', item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Knowledge Base Request not found")
    return {"detail": "Knowledge Base Request deleted"}

# Application Server Standard Endpoints
@router.get("/application-server-standard", response_model=list[ApplicationServerStandard])
async def list_application_server_standards():
    return store.list_all('application_server_standard')

@router.post("/application-server-standard", response_model=ApplicationServerStandard)
async def create_application_server_standard(item: ApplicationServerStandard):
    return store.create('application_server_standard', item)

@router.get("/application-server-standard/{item_id}", response_model=ApplicationServerStandard)
async def get_application_server_standard(item_id: str):
    item = store.get_by_id('application_server_standard', item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Application Server Standard not found")
    return item

@router.put("/application-server-standard/{item_id}", response_model=ApplicationServerStandard)
async def update_application_server_standard(item_id: str, item: ApplicationServerStandard):
    return store.update('application_server_standard', item_id, item)

@router.delete("/application-server-standard/{item_id}")
async def delete_application_server_standard(item_id: str):
    success = store.delete('application_server_standard', item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Application Server Standard not found")
    return {"detail": "Application Server Standard deleted"}

# Application Server Large Endpoints
@router.get("/application-server-large", response_model=list[ApplicationServerLarge])
async def list_application_server_larges():
    return store.list_all('application_server_large')

@router.post("/application-server-large", response_model=ApplicationServerLarge)
async def create_application_server_large(item: ApplicationServerLarge):
    return store.create('application_server_large', item)

@router.get("/application-server-large/{item_id}", response_model=ApplicationServerLarge)
async def get_application_server_large(item_id: str):
    item = store.get_by_id('application_server_large', item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Application Server Large not found")
    return item

@router.put("/application-server-large/{item_id}", response_model=ApplicationServerLarge)
async def update_application_server_large(item_id: str, item: ApplicationServerLarge):
    return store.update('application_server_large', item_id, item)

@router.delete("/application-server-large/{item_id}")
async def delete_application_server_large(item_id: str):
    success = store.delete('application_server_large', item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Application Server Large not found")
    return {"detail": "Application Server Large deleted"}

# Database Server & Oracle License Endpoints
@router.get("/database-server-oracle-license", response_model=list[DatabaseServerOracleLicense])
async def list_database_server_oracle_licenses():
    return store.list_all('database_server_oracle_license')

@router.post("/database-server-oracle-license", response_model=DatabaseServerOracleLicense)
async def create_database_server_oracle_license(item: DatabaseServerOracleLicense):
    return store.create('database_server_oracle_license', item)

@router.get("/database-server-oracle-license/{item_id}", response_model=DatabaseServerOracleLicense)
async def get_database_server_oracle_license(item_id: str):
    item = store.get_by_id('database_server_oracle_license', item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Database Server or Oracle License not found")
    return item

@router.put("/database-server-oracle-license/{item_id}", response_model=DatabaseServerOracleLicense)
async def update_database_server_oracle_license(item_id: str, item: DatabaseServerOracleLicense):
    return store.update('database_server_oracle_license', item_id, item)

@router.delete("/database-server-oracle-license/{item_id}")
async def delete_database_server_oracle_license(item_id: str):
    success = store.delete('database_server_oracle_license', item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Database Server or Oracle License not found")
    return {"detail": "Database Server or Oracle License deleted"}

# Email Account (old) Endpoints
@router.get("/email-account-old", response_model=list[EmailAccountOld])
async def list_email_accounts_old():
    return store.list_all('email_account_old')

@router.post("/email-account-old", response_model=EmailAccountOld)
async def create_email_account_old(item: EmailAccountOld):
    return store.create('email_account_old', item)

@router.get("/email-account-old/{item_id}", response_model=EmailAccountOld)
async def get_email_account_old(item_id: str):
    item = store.get_by_id('email_account_old', item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Email Account (old) not found")
    return item

@router.put("/email-account-old/{item_id}", response_model=EmailAccountOld)
async def update_email_account_old(item_id: str, item: EmailAccountOld):
    return store.update('email_account_old', item_id, item)

@router.delete("/email-account-old/{item_id}")
async def delete_email_account_old(item_id: str):
    success = store.delete('email_account_old', item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Email Account (old) not found")
    return {"detail": "Email Account (old) deleted"}