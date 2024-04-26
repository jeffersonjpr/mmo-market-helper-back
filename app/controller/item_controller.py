from ..services.item_service import ItemService
from flask import request, jsonify


class ItemController:
    def __init__(self):
        self.item_service = ItemService()

    def create(self):
        name = request.json["name"]
        description = request.json["description"]
        category_id = request.json.get("category_id")
        type_id = request.json.get("type_id")
        item = self.item_service.create(name, description, category_id, type_id)
        return jsonify(item.to_dict())

    def get(self, item_id):
        item = self.item_service.get(item_id)
        return jsonify(item.to_dict())

    def get_all(self):
        items = self.item_service.get_all()
        return jsonify([item.to_dict() for item in items])

    def update(self, item_id):
        new_name = request.json.get("name")
        new_description = request.json.get("description")
        new_category_id = request.json.get("category_id")
        new_type_id = request.json.get("type_id")
        success = self.item_service.update(item_id, new_name, new_description, new_category_id, new_type_id)
        return jsonify({"success": success})

    def delete(self, item_id):
        success = self.item_service.delete(item_id)
        return jsonify({"success": success})
