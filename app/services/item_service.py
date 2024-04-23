from ..repository.item_repository import ItemRepository

class ItemService:
    def __init__(self):
        self.item_repository = ItemRepository()

    def create(self, name, description, category_id, type_id=None):
        return self.item_repository.create(name, description, category_id, type_id)

    def get(self, item_id):
        return self.item_repository.get(item_id)
    
    def get_all(self):
        return self.item_repository.get_all()

    def update(self, item_id, new_name=None, new_description=None, new_category_id=None, new_type_id=None):
        return self.item_repository.update(item_id, new_name, new_description, new_category_id, new_type_id)

    def delete(self, item_id):
        return self.item_repository.delete(item_id)