from ..controller.market_controller import MarketController
from flask import Blueprint

market_route = Blueprint('market_route', __name__)


@market_route.route('/market', methods=['POST'])
def create():
    return MarketController().create()


@market_route.route('/market/<int:market_id>', methods=['GET'])
def get(market_id):
    return MarketController().get(market_id)


@market_route.route('/market', methods=['GET'])
def get_all():
    return MarketController().get_all()


@market_route.route('/market/<int:market_id>', methods=['PUT'])
def update(market_id):
    return MarketController().update(market_id)


@market_route.route('/market/<int:market_id>', methods=['DELETE'])
def delete(market_id):
    return MarketController().delete(market_id)
