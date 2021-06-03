"""Models for Fresh Made Easy web app."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

def connect_to_db(flask_app, db_uri='postgresql:///ratings', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

class User(db.Model):
    """A user."""

    __tablename__ = 'user'

    user_id = db.Column(db.Integer,
                        autoincrement = True,
                        primary_key = True)
    email = db.Column(db.String, unique = True)
    password = db.Column(db.String)
    fname = db.Column(db.String(25))
    lname = db.Column(db.String(25))
    username = db.Column(db.String(15))

    def __repr__(self):
        return f'<User user_id = {self.user_id} email = {self.email}>'

class Purchase(db.Model):
    """A user's purchase."""

    __tablename__ = 'purchase'

    purchase_id = db.Column(db.Integer,
                            autoincrement = True,
                            primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    date_time_of_purchase = db.Column(db.DateTime)
    payment_method_id = db.Column(db.Integer, db.ForeignKey('payment_method.payment_method_id'))
    pickup_date = db.Column(db.DateTime)
    location_id = db.Column(db.Integer, db.ForeignKey('pickup_location.location_id'))
    order_cost = db.Column(db.Integer, db.ForeignKey('item.item_cost'))

    user = db.relationship('User', backref='purchase')
    item = db.relationship('Item', backref='purchase')

    def __repr__(self):
        return f'<Purchase purchase_id = {self.purchase_id} user_id = {self.user_id} date_time_of_purchase = {self.date_time_of_purchase} payment_method_id = {self.payment_method_id} pickup_date = {self.pickup_date} location_id = {self.location_id} order_cost = {self.order_cost}>'

class Farm(db.Model):
    """A farm with items for purchase."""

    __tablename__ = 'farm'

    farm_id = db.Column(db.Integer, 
                        autoincrement = True,
                        primary_key = True)
    farm_name = db.Column(db.String(50))
    farm_address = db.Column(db.String(100))

    def __repr__(self):
        return f'<Farm farm_id = {self.farm_id} farm_name = {self.farm_name} farm_address = {self.farm_address}>'

class Item(db.Model):
    """An item available for purchase."""

    __tablename__ = 'item'

    item_id = db.Column(db.Integer, 
                        autoincrement = True,
                        primary_key = True)
    item_name = db.Column(db.String(50))
    farm_id = db.Column(db.Integer, db.ForeignKey('farm.farm_id'))
    item_cost = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'))
    item_description = db.Column(db.String)
    item_img = db.Column(db.String)

    farm = db.relationship('Farm', backref='item')
    category = db.relationship('Category', backref='item')

    def __repr__(self):
        return f'<Item item_id = {self.item_id} farm_id = {self.farm_id} item_cost = {self.item_cost} item_name = {self.item_name} category_id = {self.category_id} item_description = {self.item_description}>'

class PickupLocation(db.Model):
    """Order's pickup location."""

    __tablename__ = 'pickup_location'

    location_id = db.Column(db.Integer, 
                            autoincrement = True,
                            primary_key = True)
    location_name = db.Column(db.String(50))
    location_address = db.Column(db.String(100))
    location_neighborhood = db.Column(db.String(25))

    def __repr__(self):
        return f'<PickupLocation location_id = {self.location_id} location_name = {self.location_name} location_address = {self.location_address}>'

class Category(db.Model):
    """Item's category"""

    __tablename__ = 'category'

    category_id = db.Column(db.Integer,
                            autoincrement = True, 
                            primary_key = True)
    category_name = db.Column(db.String(50))

    def __repr__(self):
        return f'<Category category_id = {self.category_id} category_name = {self.category_name}>'

class PaymentMethod(db.Model):
    """Purchase's payment method used"""

    __tablename__ = 'payment_method'

    payment_method_id = db.Column(db.Integer, 
                                autoincrement = True, 
                                primary_key = True)
    payment_method_type = db.Column(db.String(20))
     
    def __repr__(self):
        return f'<PaymentMethod payment_method_id = {self.payment_method_id} payment_method_type = {self.payment_method_type}>'


if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    