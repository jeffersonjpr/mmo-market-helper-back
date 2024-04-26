from ..models.models import Recipe
from ..database import session
from .base_repository import BaseRepository


class RecipeRepository(BaseRepository):
    def __init__(self):
        self.model = Recipe

    def create(self, item_id, ingredient_id, quantity):
        recipe = Recipe(item_id=item_id, ingredient_id=ingredient_id, quantity=quantity)
        super().create(recipe)

    def get(self, recipe_id):
        return super().get(recipe_id)

    def get_all(self):
        return super().get_all()

    def get_by_item_id(self, item_id):
        return session.query(Recipe).filter(Recipe.item_id == item_id).all()

    def update(self, recipe_id, new_item_id=None, new_ingredient_id=None, new_quantity=None):
        recipe = self.get(recipe_id)
        if recipe:
            if new_item_id is not None:
                recipe.item_id = new_item_id
            if new_ingredient_id is not None:
                recipe.ingredient_id = new_ingredient_id
            if new_quantity is not None:
                recipe.quantity = new_quantity
            session.commit()
            return True
        return False

    def delete(self, recipe_id):
        return super().delete(recipe_id)
