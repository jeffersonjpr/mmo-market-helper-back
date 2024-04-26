from flask import Blueprint
from ..controller.item_controller import ItemController

item_route = Blueprint("item_route", __name__)


@item_route.route("/item", methods=["POST"])
def create():
    return ItemController().create()


@item_route.route("/item/<int:item_id>", methods=["GET"])
def get(item_id):
    return ItemController().get(item_id)


@item_route.route("/item", methods=["GET"])
def get_all():
    return ItemController().get_all()


@item_route.route("/item/<int:item_id>", methods=["PUT"])
def update(item_id):
    return ItemController().update(item_id)


@item_route.route("/item/<int:item_id>", methods=["DELETE"])
def delete(item_id):
    return ItemController().delete(item_id)
