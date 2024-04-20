from ..models.models import Item
from ..database import session


class ItemRepository:
    def create_item(self, name, description, category_id, type_id=None):
        item = Item(name=name, description=description,
                    category_id=category_id, type_id=type_id)
        session.add(item)
        session.commit()
        return item

    def read_item(self, item_id):
        return session.query(Item).filter(Item.id == item_id).first()

    def update_item(self, item_id, new_name=None, new_description=None, new_category_id=None, new_type_id=None):
        item = self.read_item(item_id)
        if item:
            if new_name:
                item.name = new_name
            if new_description:
                item.description = new_description
            if new_category_id:
                item.category_id = new_category_id
            if new_type_id:
                item.type_id = new_type_id
            session.commit()
            return True
        return False

    def delete_item(self, item_id):
        item = self.read_item(item_id)
        if item:
            session.delete(item)
            session.commit()
            return True
        return False
