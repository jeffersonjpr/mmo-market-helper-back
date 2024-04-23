from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


class Type(Base):
    __tablename__ = 'types'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    description = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=True)
    type_id = Column(Integer, ForeignKey('types.id'), nullable=True)

    category = relationship("Category", back_populates="items")
    type = relationship("Type", back_populates="items")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category_id': self.category_id,
            'type_id': self.type_id
        }


class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'))
    ingredient_id = Column(Integer, ForeignKey('items.id'))
    quantity = Column(Integer)

    item = relationship("Item", foreign_keys=[item_id])
    ingredient = relationship("Item", foreign_keys=[ingredient_id])


class Market(Base):
    __tablename__ = 'market'
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'))
    price = Column(Numeric)
    stack_size = Column(Integer)

    item = relationship("Item", back_populates="market")

Category.items = relationship("Item", back_populates="category")
Type.items = relationship("Item", back_populates="type")
Item.market = relationship("Market", back_populates="item")

