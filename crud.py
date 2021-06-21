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


def create_item(item_name, item_cost, item_description, item_img, farm_name, category_name):
    """Create and return a new item."""
    
    item = Item(item_name = item_name, 
            item_cost = item_cost,
            item_description = item_description, 
            item_img = item_img,
            farm_name = farm_name,
            category_name = category_name)

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


def get_all_purchases(user_id):
    """Returns all purchases made by a user."""
    user_purchases = []
    users = User.query.all()
    purchases = Purchase.query.all()

    for purchase in purchases:
        for user in users:
            if purchase.user_id == user.user_id:
                user_purchases.append([purchase.purchase_id, user.user_id])
                return purchases

    # for user in users:
    #     if user.email == email:
    #         return user.user_id

    # return Purchases.query.filter(Purchase.user_id == User.user_id)
    #started


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


def get_item_by_name(item_name):
    """Return an item's name."""
    
    items = Item.query.all()

    for item in items:
        print(item)
        if item.item_name == item_name:
            return item


def get_item_by_description(item):
    """Return an item's description."""

    items = Item.query.all()

    for item in items:
        if item.item_description == item:
            return item
    

def get_item_by_cost(item):
    """Return an item's cost."""

    items = Item.query.all()

    for item in items:
        if item.item_cost == item:
            return item


def get_farm_by_name(farm_name):
    """Return a farm's name."""

    farms = Farm.query.all()

    for farm in farms:
        if farm.farm_name == farm_name:
            return farm


def get_farm_by_address(farm):
    """Return a farm's address."""

    farms = Farm.query.all()

    for farm in farms:
        if farm.farm_address == farm:
            return farm


def get_pickup_location_by_name(location_name):
    """Return a pickup location's name."""

    locations = PickupLocation.query.all()

    for location in locations:
        if location.location_name == location_name:
            return location


def get_pickup_location_by_address(location):
    """Return a pickup location's address."""

    locations = PickupLocation.query.all()

    for location in locations:
        if location.location_address == location:
            return location


def get_pickup_location_by_neighborhood(location):
    """Return a pickup location's neighborhood."""

    locations = PickupLocation.query.all()

    for location in locations:
        if location.neighborhood_name == location:
            return location.neighborhood_name


def create_new_purchase(user_id, items, date_time_of_purchase, payment_method, pickup_date, pickup_location, purchase_total):
    """Creates a new user purchase."""

    purchase = Purchase(user_id = user_id, items = items, date_time_of_purchase = date_time_of_purchase, payment_method = payment_method, pickup_date = pickup_date, pickup_location = pickup_location, purchase_total = purchase_total)

    db.session.add(purchase)
    db.session.commit()

    return purchase


def get_user_id_by_email(email):

    users = User.query.all()

    for user in users:
        if user.email == email:
            return user.user_id


def get_pickup_location_id(location):
    """Return a pickup location's id."""

    locations = PickupLocation.query.all()

    for location in locations:
        if location.neighborhood_name == location:
            return location.location_id


def get_payment_method_id(payment_method):
    """Returns a payment methods' id."""

    methods = PaymentMethod.query.all()

    for method in methods:
        if method.payment_method_type == payment_method:
            return method.payment_method_id



if __name__ == '__main__':
    from server import app
    connect_to_db(app)