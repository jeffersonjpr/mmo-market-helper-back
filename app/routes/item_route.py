from flask import Blueprint
from ..controller.item_controller import ItemController

item_route = Blueprint('item_route', __name__)

@item_route.route('/item', methods=['POST'])
def create_item():
    return ItemController().create_item()

@item_route.route('/item/<int:item_id>', methods=['GET'])
def read_item(item_id):
    return ItemController().read_item(item_id)

@item_route.route('/item/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    return ItemController().update_item(item_id)

@item_route.route('/item/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    return ItemController().delete_item(item_id)