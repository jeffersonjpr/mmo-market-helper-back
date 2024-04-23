from ..models.models import Market
from ..database import session

class MarketRepository:
    def create(self, item_id, price, stack_size):
        market = Market(item_id=item_id, price=price, stack_size=stack_size)
        session.add(market)
        session.commit()
        return market

    def get(self, market_id):
        return session.query(Market).filter(Market.id == market_id).first()
    
    def get_all(self):
        return session.query(Market).all()

    def update(self, market_id, new_price, new_stack_size):
        market = self.get(market_id)
        if market:
            market.price = new_price
            market.stack_size = new_stack_size
            session.commit()
            return True
        return False

    def delete(self, market_id):
        market = self.get(market_id)
        if market:
            session.delete(market)
            session.commit()
            return True
        return False