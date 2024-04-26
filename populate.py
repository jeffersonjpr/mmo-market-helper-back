from app.services.category_service import CategoryService
from app.services.item_service import ItemService
from app.services.type_service import TypeService
from app.services.market_service import MarketService

category_service = CategoryService()
item_service = ItemService()
type_service = TypeService()
market_service = MarketService()

# Populate the database with some initial data
def populate_type():
    types = ['Resource', 'Item']
    for type in types:
        if not type_service.get_by_name(type):
            type_service.create(type)

    print('Types:')
    for type in type_service.get_all():
        print(type.to_dict())

def populate_category():
    categories = ['Mineral', 'Plant', 'Animal']
    for category in categories:
        if not category_service.get_by_name(category):
            category_service.create(category)

    print('Categories:')
    for category in category_service.get_all():
        print(category.to_dict())


if __name__ == '__main__':
    populate_type()
