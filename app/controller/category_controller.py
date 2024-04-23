from ..services.category_service import CategoryService
from flask import request, jsonify


class CategoryController:
    def __init__(self):
        self.category_service = CategoryService()

    def create(self):
        name = request.json['name']
        category = self.category_service.create(name)
        return jsonify(category.to_dict())

    def get(self, category_id):
        category = self.category_service.get(category_id)
        return jsonify(category.to_dict())

    def get_all(self):
        categories = self.category_service.get_all()
        return jsonify([category.to_dict() for category in categories])

    def update(self, category_id):
        new_name = request.json.get('name')
        success = self.category_service.update(category_id, new_name)
        return jsonify({'success': success})

    def delete(self, category_id):
        success = self.category_service.delete(category_id)
        return jsonify({'success': success})
