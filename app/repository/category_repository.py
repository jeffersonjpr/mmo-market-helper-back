from models.models import Category
from database import session

def create_category(name):
    category = Category(name=name)
    session.add(category)
    session.commit()
    return category


def read_category(category_id):
    return session.query(Category).filter(Category.id == category_id).first()


def update_category(category_id, new_name):
    category = read_category(category_id)
    if category:
        category.name = new_name
        session.commit()
        return True
    return False


def delete_category(category_id):
    category = read_category(category_id)
    if category:
        session.delete(category)
        session.commit()
        return True
    return False
