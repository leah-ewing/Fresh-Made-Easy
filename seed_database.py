"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb fresh')
os.system('createdb fresh')

model.connect_to_db(server.app)
model.db.create_all()


with open('data/farms.json') as f:
    farm_data = json.loads(f.read())

with open('data/items.json') as i:
    item_data = json.loads(i.read())

with open('data/item-categories.json') as c:
    category_data = json.loads(c.reads())

with open('payment-methods') as p:
    payment_data = json.loads(p.read())

with open('data/pickup-locations') as l:
    pickup_location_data = json.loads(l.read())


users_in_db = []
for user in user_data:
    email, password, fname, lname, username = (user['email'],
                                                user['password'],
                                                user['fname'],
                                                user['lname'],
                                                user['username'])

db_user = crud.create_user(email, password, fname, lname, username)
users_in_db.append(db.farm)



farms_in_db = []
for farm in farm_data:
    farm_name, farm_address = (farm['farm_name'],
                                farm['farm_address'])

db_farm = crud.create_farm(farm_name, farm_address)
farms_in_db.append(db.farm)



items_in_db = []
for item in item_data:
    item_name, item_cost, item_description, item_img = (item['item_name'],
                                                        item_cost['item_cost'],
                                                        item_description['item_description'],
                                                        item_img['item_img'])
    farm_id = farm['farm_id']
    category_name = category['category_name']

db_farm = crud.create_item(item_name, farm_id, item_cost, item_description, item_img)
items_in_db.append(db_item)



categories_in_db = []
for category in category_data:
    category_name = category['category_name']

db_category = crud.create_category(category_name)
categories_in_db.append(db_category)



payment_methods_in_db = []
for payment_method in payment_data:
    payment_method_type = payment_method['payment_method_type']

db_payment_method = crud.create_payment_method(payment_method_type)
payment_methods_in_db.append(db_payment_method)



pickup_locations_in_db = []
for pickup_location in pickup_location_data:
    location_name, location_address, location_neighborhood = (pickup_location['location_name'],
                                                            location_address['location_address'],
                                                            location_neighborhood['location_neighborhood'])
pickup_locations_in_db = crud.create_pickup_location(pickup_location)
pickup_locations_in_db.append(db.pickup_location)



