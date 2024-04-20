from models import Market
from database import session


def create_market(item_id, price, stack_size):
    market = Market(item_id=item_id, price=price, stack_size=stack_size)
    session.add(market)
    session.commit()
    return market


def read_market(market_id):
    return session.query(Market).filter(Market.id == market_id).first()


def update_market(market_id, new_price=None, new_stack_size=None):
    market = read_market(market_id)
    if market:
        if new_price is not None:
            market.price = new_price
        if new_stack_size is not None:
            market.stack_size = new_stack_size
        session.commit()
        return True
    return False


def delete_market(market_id):
    market = read_market(market_id)
    if market:
        session.delete(market)
        session.commit()
        return True
    return False
