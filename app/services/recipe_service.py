from ..repository.recipe_repository import RecipeRepository
from ..models.models import Recipe


class RecipeService:
    def __init__(self):
        self.recipe_repository = RecipeRepository()

    def create(self, item_id, ingredients):
        recipes = []
        for ingredient_id, quantity in ingredients:
            recipe = Recipe(item_id=item_id, ingredient_id=ingredient_id, quantity=quantity)
            self.recipe_repository.create(recipe)
        return recipes

    def get(self, recipe_id):
        return self.recipe_repository.get(recipe_id)

    def get_all(self):
        return self.recipe_repository.get_all()

    def get_by_item_id(self, item_id):
        return self.recipe_repository.get_by_item_id(item_id)

    def update(self, recipe_id, new_item_id=None, new_ingredient_id=None, new_quantity=None):
        return self.recipe_repository.update(recipe_id, new_item_id, new_ingredient_id, new_quantity)

    def delete(self, recipe_id):
        return self.recipe_repository.delete(recipe_id)
