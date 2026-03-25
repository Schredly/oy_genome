class EquipmentStore:
    data = {}

    @classmethod
    def create(cls, equipment):
        cls.data[equipment.name] = equipment.dict()

    @classmethod
    def get_by_id(cls, equipment_id):
        return cls.data.get(equipment_id)

    @classmethod
    def list_all(cls):
        return list(cls.data.values())

    @classmethod
    def update(cls, equipment_id, equipment):
        if equipment_id in cls.data:
            cls.data[equipment_id] = equipment.dict()

    @classmethod
    def delete(cls, equipment_id):
        if equipment_id in cls.data:
            del cls.data[equipment_id]