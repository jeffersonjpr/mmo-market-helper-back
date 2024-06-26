from ..models.models import Type
from ..database import session
from .base_repository import BaseRepository


class TypeRepository(BaseRepository):
    def __init__(self):
        self.model = Type

    def create(sefl, name):
        type = Type(name=name)
        return super().create(type)

    def get(self, type_id):
        super().get(type_id)

    def get_all(self):
        return super().get_all()

    def get_by_name(self, name):
        return super().get_by_name(name)

    def update(self, type_id, new_name):
        type = self.get(type_id)
        if type:
            type.name = new_name
            session.commit()
            return True
        return False

    def delete(self, type_id: int) -> bool:
        return super().delete(type_id)
