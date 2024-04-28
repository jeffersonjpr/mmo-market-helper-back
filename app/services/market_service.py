from ..repository.market_repository import MarketRepository


class MarketService:
    def __init__(self):
        self.market_repository = MarketRepository()

    def create(self, item_id, price, stack_size):
        return self.market_repository.create(item_id, price, stack_size)

    def get(self, market_id):
        return self.market_repository.get(market_id)

    def get_all(self):
        return self.market_repository.get_all()
    
    def get_all_by_item_id(self, item_id):
        return self.market_repository.get_all_by_item_id(item_id)

    def update(self, market_id, new_price, new_stack_size):
        return self.market_repository.update(market_id, new_price, new_stack_size)

    def delete(self, market_id):
        return self.market_repository.delete(market_id)

    def get_avg_price(self, item_id):
        return self.market_repository.get_avg_price(item_id)