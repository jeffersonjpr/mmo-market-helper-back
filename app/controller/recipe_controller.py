from ..services.recipe_service import RecipeService
from flask import request, jsonify


class RecipeController:
    def __init__(self):
        self.recipe_service = RecipeService()

    def create(self):
        item_id = request.json.get("item_id")
        ingredients = request.json.get("ingredients")
        recipes = self.recipe_service.create(item_id, ingredients)
        return jsonify(recipes)

    def get(self, recipe_id):
        recipe = self.recipe_service.get(recipe_id)
        return jsonify(recipe)

    def get_all(self):
        recipes = self.recipe_service.get_all()
        return jsonify(recipes)

    def get_by_item_id(self, item_id):
        recipes = self.recipe_service.get_by_item_id(item_id)
        return jsonify(recipes)

    def update(self, recipe_id):
        new_item_id = request.json.get("new_item_id")
        new_ingredient_id = request.json.get("new_ingredient_id")
        new_quantity = request.json.get("new_quantity")
        success = self.recipe_service.update(recipe_id, new_item_id, new_ingredient_id, new_quantity)
        return jsonify(success)

    def delete(self, recipe_id):
        success = self.recipe_service.delete(recipe_id)
        return jsonify(success)
