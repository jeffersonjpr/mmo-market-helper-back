from ..models.models import Type
from ..database import session


class TypeRepository:
    def create(sefl, name):
        type = Type(name=name)
        session.add(type)
        session.commit()
        return type

    def get(self, type_id):
        return session.query(Type).filter(Type.id == type_id).first()
    
    def get_all(self):
        return session.query(Type).all()

    def update(self, type_id, new_name):
        type = self.get(type_id)
        if type:
            type.name = new_name
            session.commit()
            return True
        return False

    def delete(self, type_id):
        type = self.get(type_id)
        if type:
            session.delete(type)
            session.commit()
            return True
        return False
