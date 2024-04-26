from ..models.models import Category
from ..database import session


class CategoryRepository:
    def create(self, name):
        category = Category(name=name)
        session.add(category)
        session.commit()
        return category

    def get(self, category_id):
        return session.query(Category).filter(Category.id == category_id).first()

    def get_all(self):
        return session.query(Category).all()
    
    def get_by_name(self, name):
        return session.query(Category).filter(Category.name == name).first()

    def update(self, category_id, new_name):
        category = self.get(category_id)
        if category:
            category.name = new_name
            session.commit()
            return True
        return False

    def delete(self, category_id):
        category = self.get(category_id)
        if category:
            session.delete(category)
            session.commit()
            return True
        return False
