from ..models.models import Item
from ..database import session


class ItemRepository:
    def create(self, name, description, category_id=None, type_id=None):
        item = Item(name=name, description=description, category_id=category_id, type_id=type_id)
        session.add(item)
        session.commit()
        return item

    def get(self, item_id):
        return session.query(Item).filter(Item.id == item_id).first()

    def get_all(self):
        return session.query(Item).all()

    def update(
        self,
        item_id,
        new_name=None,
        new_description=None,
        new_category_id=None,
        new_type_id=None,
    ):
        item = self.get(item_id)
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

    def delete(self, item_id):
        item = self.get(item_id)
        if item:
            session.delete(item)
            session.commit()
            return True
        return False
