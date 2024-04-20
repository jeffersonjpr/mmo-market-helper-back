# crud.py

from models import session, Recipe

# Example usage
#ingredients = [(ingredient1_id, quantity1), (ingredient2_id, quantity2), ...]
#create_recipe(item_id, ingredients)

def create_recipe(item_id, ingredients):
    recipes = []
    for ingredient_id, quantity in ingredients:
        recipe = Recipe(item_id=item_id,
                        ingredient_id=ingredient_id, quantity=quantity)
        session.add(recipe)
        recipes.append(recipe)
    session.commit()
    return recipes


def read_recipe(recipe_id):
    return session.query(Recipe).filter(Recipe.id == recipe_id).first()


def update_recipe(recipe_id, new_item_id=None, new_ingredient_id=None, new_quantity=None):
    recipe = read_recipe(recipe_id)
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


def delete_recipe(recipe_id):
    recipe = read_recipe(recipe_id)
    if recipe:
        session.delete(recipe)
        session.commit()
        return True
    return False
