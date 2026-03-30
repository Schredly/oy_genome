from typing import Any, Dict, List, Optional
from uuid import uuid4
from .models import ServerReboot, DatabaseRestore, BeachEquipmentRental, RequestKnowledgeBase, ApplicationServerStandard, ApplicationServerLarge, DatabaseServerOracleLicense, EmailAccountOld

class Store:
    def __init__(self):
        self.data: Dict[str, Dict[str, Any]] = {
            'server_reboot': {},
            'database_restore': {},
            'beach_equipment_rental': {},
            'request_knowledge_base': {},
            'application_server_standard': {},
            'application_server_large': {},
            'database_server_oracle_license': {},
            'email_account_old': {}
        }

    def generate_id(self) -> str:
        return str(uuid4())

    def create(self, entity_type: str, item: Any) -> Any:
        item_id = self.generate_id()
        self.data[entity_type][item_id] = item.dict()
        return self.data[entity_type][item_id]

    def get_by_id(self, entity_type: str, item_id: str) -> Optional[Dict]:
        return self.data[entity_type].get(item_id)

    def list_all(self, entity_type: str) -> List[Dict]:
        return list(self.data[entity_type].values())

    def update(self, entity_type: str, item_id: str, item: Any) -> Optional[Dict]:
        if item_id in self.data[entity_type]:
            self.data[entity_type][item_id] = item.dict()
            return self.data[entity_type][item_id]
        return None

    def delete(self, entity_type: str, item_id: str) -> bool:
        if item_id in self.data[entity_type]:
            del self.data[entity_type][item_id]
            return True
        return False