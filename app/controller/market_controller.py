from ..services.market_service import MarketService
from flask import request, jsonify


class MarketController:
    def __init__(self):
        self.market_service = MarketService()

    def create(self):
        name = request.json['name']
        market = self.market_service.create(name)
        return jsonify(market.to_dict())

    def get(self, market_id):
        market = self.market_service.get(market_id)
        return jsonify(market.to_dict())

    def get_all(self):
        markets = self.market_service.get_all()
        return jsonify([market.to_dict() for market in markets])

    def update(self, market_id):
        new_name = request.json.get('name')
        success = self.market_service.update(market_id, new_name)
        return jsonify({'success': success})

    def delete(self, market_id):
        success = self.market_service.delete(market_id)
        return jsonify({'success': success})
