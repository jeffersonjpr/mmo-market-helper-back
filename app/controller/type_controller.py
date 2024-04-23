from ..services.type_service import TypeService
from flask import request, jsonify

class TypeController:
    def __init__(self):
        self.type_service = TypeService()

    def create(self):
        name = request.json['name']
        type = self.type_service.create(name)
        return jsonify(type.to_dict())

    def get(self, type_id):
        type = self.type_service.get(type_id)
        return jsonify(type.to_dict())

    def get_all(self):
        types = self.type_service.get_all()
        return jsonify([type.to_dict() for type in types])

    def update(self, type_id):
        new_name = request.json.get('name')
        success = self.type_service.update(type_id, new_name)
        return jsonify({'success': success})

    def delete(self, type_id):
        success = self.type_service.delete(type_id)
        return jsonify({'success': success})