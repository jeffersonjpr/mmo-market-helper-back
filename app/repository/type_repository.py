from models import Type
from database import session


class TypeRepository:
    def create_type(sefl, name):
        type = Type(name=name)
        session.add(type)
        session.commit()
        return type

    def read_type(self, type_id):
        return session.query(Type).filter(Type.id == type_id).first()

    def update_type(self, type_id, new_name):
        type = self.read_type(type_id)
        if type:
            type.name = new_name
            session.commit()
            return True
        return False

    def delete_type(self, type_id):
        type = self.read_type(type_id)
        if type:
            session.delete(type)
            session.commit()
            return True
        return False
