"""CRUD operations."""

from model import db, User, Purchase, Farm, Item, PickupLocation, Category, PaymentMethod, connect_to_db



def create_user(email, password, fname, lname, username):
    """Create and return a new user."""

    user = User(email = email, 
                password = password, 
                fname = fname,
                lname = lname,
                username = username)
    
    db.session.add(user)
    db.session.commit()

    return user

# def create_neighborhood(neighborhood_name):
#     """Create and return a new neighborhood in Nashville."""

#     neighborhood = Neighborhood(neighborhood_name = neighborhood_name)

#     db.session.add(neighborhood)
#     db.session.commit()

#     return neighborhood


def create_farm(farm_name, farm_address):
    """Create and return a new farm."""

    farm = Farm(farm_name = farm_name, farm_address = farm_address)
    db.session.add(farm)
    db.session.commit()

    return farm


def create_item(item_name, item_cost, item_description, item_img):
    """Create and return a new item."""
    
    item = Item(item_name = item_name, 
            item_cost = item_cost,
            item_description = item_description, 
            item_img = item_img)

    db.session.add(item)
    db.session.commit()

    return item


def create_category(category_name):
    """Create and return a new item category."""

    category = Category(category_name = category_name)
    
    db.session.add(category)
    db.session.commit()

    return category


def create_pickup_location(location_name, location_address):
    """Create and return a new order pickup location."""

    pickup_location = PickupLocation(location_name = location_name,
                                    location_address = location_address)

    db.session.add(pickup_location)
    db.session.commit()

    return pickup_location


def create_payment_method(payment_method_type):
    """Create and return a new payment method."""

    payment_method = PaymentMethod(payment_method_type = payment_method_type)

    db.session.add(payment_method)
    db.session.commit()

    return payment_method


def get_all_purchases():
    """Returns all purchases made."""

    return Purchases.query.all()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)