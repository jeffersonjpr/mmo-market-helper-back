from sqlalchemy import Numeric, func
from ..models.models import Market
from ..database import session
from .base_repository import BaseRepository


class MarketRepository(BaseRepository):
    def __init__(self):
        self.model = Market

    def create(self, item_id, price, stack_size):
        market = Market(item_id=item_id, price=price, stack_size=stack_size)
        super().create(market)

    def get(self, market_id: int):
        return super().get(market_id)

    def get_all(self):
        return super().get_all()

    def get_all_by_item_id(self, item_id: int):
        return session.query(Market).filter(Market.item_id == item_id).all()

    def get_avg_price(self, item_id: int):
        stack_sizes = self.get_stack_sizes_list(item_id)
        avg_prices = []
        for stack_size in stack_sizes:
            price = self.get_price_by_stack_size(item_id, stack_size)
            avg_price = price / stack_size

    def get_avg_price(self, item_id):
        subquery = session.query(func.max(Market.id).label(
            'max_id')).group_by(Market.stack_size).subquery()
        avg_price = session.query(func.avg(Market.price / Market.stack_size)).filter(
            Market.item_id == item_id).join(subquery, Market.id == subquery.c.max_id).scalar()
        return avg_price

    def get_stack_sizes_list(self, item_id: int):
        return session.query(Market.stack_size).filter(Market.item_id == item_id).all()

    def get_price_by_stack_size(self, item_id: int, stack_size: int):
        return session.query(Market.price).filter(Market.item_id == item_id, Market.stack_size == stack_size).first()

    def update(self, market_id: int, new_price: Numeric, new_stack_size: int) -> bool:
        market = self.get(market_id)
        if market:
            market.price = new_price
            market.stack_size = new_stack_size
            session.commit()
            return True
        return False

    def delete(self, market_id: int) -> bool:
        return super().delete(market_id)
