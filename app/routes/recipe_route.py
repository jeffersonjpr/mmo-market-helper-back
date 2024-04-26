from flask import Blueprint
from ..controller.recipe_controller import RecipeController

recipe_route = Blueprint("recipe_route", __name__)


@recipe_route.route("/recipe", methods=["POST"])
def create():
    return RecipeController().create()


@recipe_route.route("/recipe/<int:recipe_id>", methods=["GET"])
def get(recipe_id):
    return RecipeController().get(recipe_id)


@recipe_route.route("/recipe", methods=["GET"])
def get_all():
    return RecipeController().get_all()


@recipe_route.route("/recipe/item/<int:item_id>", methods=["GET"])
def get_by_item_id(item_id):
    return RecipeController().get_by_item_id(item_id)


@recipe_route.route("/recipe/<int:recipe_id>", methods=["PUT"])
def update(recipe_id):
    return RecipeController().update(recipe_id)


@recipe_route.route("/recipe/<int:recipe_id>", methods=["DELETE"])
def delete(recipe_id):
    return RecipeController().delete(recipe_id)
