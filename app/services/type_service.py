from ..repository.type_repository import TypeRepository

class TypeService:
    def __init__(self):
        self.type_repository = TypeRepository()

    def create(self, name):
        return self.type_repository.create(name)

    def get(self, type_id):
        return self.type_repository.get(type_id)
    
    def get_all(self):
        return self.type_repository.get_all()
    
    def get_by_name(self, name):
        return self.type_repository.get_by_name(name)

    def update(self, type_id, new_name):
        return self.type_repository.update(type_id, new_name)

    def delete(self, type_id):
        return self.type_repository.delete(type_id)