"""CRUD operations."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from model import db, User, Purchase, Farm, Item, PickupLocation, Category, PaymentMethod, ShoppingCart, PurchaseItems, CartItems, connect_to_db


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


def create_farm(farm_name, farm_address, farm_description):
    """Create and return a new farm."""

    farm = Farm(farm_name = farm_name, farm_address = farm_address, farm_description = farm_description)
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


def create_new_cart(user_id):
    """Creates a new user shopping cart."""

    shopping_cart = ShoppingCart(user_id = user_id)

    db.session.add(shopping_cart)
    db.session.commit()

    return shopping_cart


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


def get_category_by_name(category_name):
    """Returns a category given a name."""

    categories = Category.query.all()

    for category in categories:
        if category.category_name == category_name:
            return category


def get_item_by_category(category_name):
    """Returns items given a category name"""

    items = Item.query.all()

    for item in items:
        if item.category_name == category_name:
            return item


def get_purchase_id(user_id):
    """Returns purchase id's for a given user"""

    purchases = Purchase.query.all()

    for purchase in purchases:
        if purchase.user_id == user_id:
            return purchase.purchase_id


def add_item_to_cart(item_id, user_id, item_amount):
    """Adds an item to a user's cart."""

    cart_items = CartItems(item_id = item_id, user_id = user_id, item_amount = item_amount)
    shopping_cart = ShoppingCart(user_id = user_id)
    
    db.session.add(cart_items)
    db.session.add(shopping_cart)
    db.session.commit()

    return cart_items


def get_item_id_by_name(item_name):
    """Gets an item id based on a given name."""

    items = Item.query.all()

    for item in items:
        if item.item_name == item_name:
            return item.item_id


def get_item_name_by_id(item_id):
    """Gets an item based on a given id."""

    items = Item.query.all()

    for item in items:
        if item.item_id == item_id:
            return items.item_name


def get_item_cost(item_id):
    """Return an item's cost."""

    items = Item.query.all()

    for item in items:
        if item.item_id == item_id:
            return item.item_cost


def get_cart_id_by_user_id(user_id):
    """Returns id's of items in a user's shopping cart."""

    cart_item_ids = CartItems.query.all()

    for cart_item_id in cart_item_ids:
        if cart_item_id.user_id == user_id:
            return cart_item_ids


def get_item_names_in_cart(user_id):
    """Returns names of items in a user's cart."""

    cart_items = set()
    item_ids = CartItems.query.all()
    items = Item.query.all()
    item_amounts = []

    for item_id in item_ids:
        for item in items:
            if item_id.user_id == user_id:
                if item_id.item_id == item.item_id:
                    cart_items.add(item.item_name)
    return (cart_items)


def get_cart_total(user_id):

    item_totals = []
    items_in_cart = CartItems.query.all()
    items = Item.query.all()

    for item_in_cart in items_in_cart:
        for item in items:
            if item_in_cart.user_id == user_id:
                if item_in_cart.item_id == item.item_id:
                    item_totals.append(item.item_cost * item_in_cart.item_amount)
    return sum(item_totals)


def delete_all_cart_items(user):
    """Deletes all items from a user's cart."""

    delete_items = f"DELETE FROM cart_items WHERE user_id = {user}"

    db.session.execute(delete_items)

    db.session.commit()


def get_item_ids_in_cart(user_id):
    """Returns ids of items in a user's cart."""

    items_in_cart = CartItems.query.all()
    items = Item.query.all()
    item_ids = set()

    for item_in_cart in items_in_cart:
        for item in items:
            if item_in_cart.user_id == user_id:
                item_ids.add(item_in_cart.item_id)
    return (item_ids)


def create_new_purchase(user_id, date_time_of_purchase, payment_method, pickup_date, pickup_location, purchase_total):
    """Creates a new user purchase."""

    items_in_cart = CartItems.query.all()
    items = Item.query.all()
    item_ids = set()

    purchase = Purchase(user_id = user_id, date_time_of_purchase = date_time_of_purchase, payment_method = payment_method, pickup_date = pickup_date, pickup_location = pickup_location, purchase_total = purchase_total)
    db.session.add(purchase)
    db.session.commit()

    for item_in_cart in items_in_cart:
        for item in items:
            if item_in_cart.user_id == user_id:
                item_ids.add(item_in_cart.item_id)
    for item_id in item_ids:
        purchase_items = PurchaseItems(item_id = item_id, purchase_id = purchase.purchase_id, user_id = user_id)
        db.session.add(purchase_items)
        db.session.commit()


def get_all_purchase_ids(user_id):
    """Returns ids of all purchases from a user."""

    purchases = PurchaseItems.query.all()
    purchase_ids = set()

    for purchase in purchases:
        if purchase.user_id == user_id:
            purchase_ids.add(purchase.purchase_id)
    return purchase_ids
    

def get_all_user_purchases(user_id):
    """Returns all purchases from a user."""

    purchases = Purchase.query.all()
    purchase_items = PurchaseItems.query.all()
    purchase_ids = set()
    user_purchases = []

    for purchase_item in purchase_items:
        if purchase_item.user_id == user_id:
            purchase_ids.add(purchase_item.purchase_id)
    for purchase_id in purchase_ids:
        for purchase in purchases:
            if purchase.purchase_id == purchase_id:
                user_purchases.append(purchase)
    return user_purchases


def get_purchase_by_id(purchase_id):
    """Returns a purchase given a purchase ID."""

    purchases = Purchase.query.all()
    # user_purchases = []

    for purchase in purchases:
        if purchase.purchase_id == int(purchase_id):
            return purchase


def get_current_purchase(current_purchase):
    return current_purchase


def get_item_names_by_farm_name(farm_name):
    """Returns item names from a given farm."""

    farms = Farm.query.all()
    items = Item.query.all()
    farm_items = set()

    for farm in farms:
        for item in items:
            if item.farm_name == farm_name:
                farm_items.add(item.item_name)
    return farm_items


def get_item_names_by_category_name(category_name):
    """Returns item names from a given category."""

    categories = Category.query.all()
    items = Item.query.all()
    category_items = set()

    for category in categories:
        for item in items:
            if item.category_name == category_name:
                category_items.add(item.item_name)
    return category_items


def get_items_in_purchase(purchase_id):
    """Returns item names in a user's purchase."""

    purchase_items = PurchaseItems.query.all()
    items = Item.query.all()
    item_ids = set()
    item_names = set()
    

    for purchase_item in purchase_items:
        if purchase_item.purchase_id == purchase_id:
            item_ids.add(purchase_item.item_id)
    # return item_ids
    for item in items:
        for item_id in item_ids:
            if item.item_id == item_id:
                item_names.add(item.item_name)
    return item_names


if __name__ == '__main__':
    from server import app
    connect_to_db(app)