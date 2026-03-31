from typing import Dict, List
from .models import UpdateSet

class InMemoryStore:
    def __init__(self):
        self.data = {}

    def create(self, item: Dict):
        self.data[item['sys_id']] = item

    def get_by_id(self, item_id: str) -> Dict:
        return self.data.get(item_id, None)

    def list_all(self) -> List[Dict]:
        return list(self.data.values())

    def update(self, item_id: str, item: Dict):
        if item_id in self.data:
            self.data[item_id].update(item)

    def delete(self, item_id: str):
        if item_id in self.data:
            del self.data[item_id]

# Initialize store for update sets
update_set_store = InMemoryStore()