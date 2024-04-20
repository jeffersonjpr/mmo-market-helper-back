from ..services.item_service import ItemService
from flask import request, jsonify

class ItemController:
    def __init__(self):
        self.item_service = ItemService()

    def create_item(self):
        name = request.json['name']
        description = request.json['description']
        category_id = request.json['category_id']
        type_id = request.json.get('type_id')
        item = self.item_service.create_item(name, description, category_id, type_id)
        return jsonify(item.serialize())

    def read_item(self, item_id):
        item = self.item_service.read_item(item_id)
        return jsonify(item.serialize())

    def update_item(self, item_id):
        new_name = request.json.get('name')
        new_description = request.json.get('description')
        new_category_id = request.json.get('category_id')
        new_type_id = request.json.get('type_id')
        success = self.item_service.update_item(item_id, new_name, new_description, new_category_id, new_type_id)
        return jsonify({'success': success})

    def delete_item(self, item_id):
        success = self.item_service.delete_item(item_id)
        return jsonify({'success': success})