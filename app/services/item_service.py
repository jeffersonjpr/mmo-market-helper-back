from ..repository.item_repository import ItemRepository

class ItemService:
    def __init__(self):
        self.item_repository = ItemRepository()

    def create_item(self, name, description, category_id, type_id=None):
        return self.item_repository.create_item(name, description, category_id, type_id)

    def read_item(self, item_id):
        return self.item_repository.read_item(item_id)

    def update_item(self, item_id, new_name=None, new_description=None, new_category_id=None, new_type_id=None):
        return self.item_repository.update_item(item_id, new_name, new_description, new_category_id, new_type_id)

    def delete_item(self, item_id):
        return self.item_repository.delete_item(item_id)