from flask import Blueprint
from ..controller.type_controller import TypeController

type_route = Blueprint("type_route", __name__)


@type_route.route("/type", methods=["POST"])
def create():
    return TypeController().create()


@type_route.route("/type/<int:type_id>", methods=["GET"])
def get(type_id):
    return TypeController().get(type_id)


@type_route.route("/type", methods=["GET"])
def get_all():
    return TypeController().get_all()


@type_route.route("/type/<int:type_id>", methods=["PUT"])
def update(type_id):
    return TypeController().update(type_id)


@type_route.route("/type/<int:type_id>", methods=["DELETE"])
def delete(type_id):
    return TypeController().delete(type_id)
