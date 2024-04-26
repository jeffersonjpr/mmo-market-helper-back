from ..repository.category_repository import CategoryRepository


class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository()

    def create(self, name):
        return self.category_repository.create(name)

    def get(self, category_id):
        return self.category_repository.get(category_id)

    def get_all(self):
        return self.category_repository.get_all()
    
    def get_by_name(self, name):
        return self.category_repository.get_by_name(name)

    def update(self, category_id, new_name):
        return self.category_repository.update(category_id, new_name)

    def delete(self, category_id):
        return self.category_repository.delete(category_id)
