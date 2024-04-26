from flask import Blueprint
from ..controller.category_controller import CategoryController

category_route = Blueprint('category_route', __name__)


@category_route.route('/category', methods=['POST'])
def create():
    return CategoryController().create()


@category_route.route('/category/<int:category_id>', methods=['GET'])
def get(category_id):
    return CategoryController().get(category_id)


@category_route.route('/category', methods=['GET'])
def get_all():
    return CategoryController().get_all()


@category_route.route('/category/<int:category_id>', methods=['PUT'])
def update(category_id):
    return CategoryController().update(category_id)


@category_route.route('/category/<int:category_id>', methods=['DELETE'])
def delete(category_id):
    return CategoryController().delete(category_id)
