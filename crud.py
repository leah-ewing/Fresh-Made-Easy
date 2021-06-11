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


def create_pickup_location(location_name, location_address, neighborhood_name):
    """Create and return a new order pickup location."""

    pickup_location = PickupLocation(location_name = location_name,
                                    location_address = location_address,
                                    neighborhood_name = neighborhood_name)

    db.session.add(pickup_location)
    db.session.commit()

    return pickup_location


def create_payment_method(payment_method_type):
    """Create and return a new payment method."""

    payment_method = PaymentMethod(payment_method_type = payment_method_type)

    db.session.add(payment_method)
    db.session.commit()

    return payment_method


def get_all_purchases(user):
    """Returns all purchases made by a user."""

    return Purchases.query.all()
    #started!


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


def user_username(email):
    """Return a username by email."""

    return User.query.filter(User.username == email).first()


def get_user_by_username(email):
    """Return a user by username."""

    users = User.query.all()

    for user in users:
        if user.email == email:
            return user.username


def login_user(email, password):
    """Returns a user by email and password."""

    return User.query.filter(User.email == email, User.password == password).first()


def get_user_fname(email):
    """Return a user's first name by email."""

    users = User.query.all()

    for user in users:
        if user.email == email:
            return user.fname


def get_user_lname(email):
    """Return a user's last name by email."""

    users = User.query.all()

    for user in users:
        if user.email == email:
            return user.lname


def get_item_name(item):
    """Return an item's name."""

    items = Item.query.all()

    for item in items:
        if item.item_name == item:
            return item.item_name


def get_item_description(item):
    """Return an item's description."""

    items = Item.query.all()

    for item in items:
        if item.item_description == item:
            return item.item_description
    

def get_item_cost(item):
    """Return an item's cost."""

    items = Item.query.all()

    for item in items:
        if item.item_cost == item:
            return item.item_cost



if __name__ == '__main__':
    from server import app
    connect_to_db(app)