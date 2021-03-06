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


with open('static/farms.json') as f:
    farm_data = json.loads(f.read())
    # farms

with open('static/items.json') as i:
    item_data = json.loads(i.read())
    print(item_data)
    # items

with open('static/item-categories.json') as c:
    category_data = json.loads(c.read())
    # item categories

with open('static/payment-methods.json') as p:
    payment_data = json.loads(p.read())
    # payment methods

with open('static/pickup-locations.json') as l:
    pickup_location_data = json.loads(l.read())
    # pickup locations


"""Farms"""
farms_in_db = []
for farm in farm_data:
    farm_name, farm_address, farm_description = (farm['farm_name'],
                               farm['farm_address'],
                               farm['farm_description'])
                                                
    db_farm = crud.create_farm(farm_name, farm_address, farm_description)
    farms_in_db.append(db_farm)


"""Items"""
items_in_db = []
for item in item_data:
    item_name, item_cost, item_description, item_img, farm_name, category_name = (item['item_name'],
                                                        item['item_cost'],
                                                        item['item_description'],
                                                        item['item_img'],
                                                        item['farm_name'],
                                                        item['category_name'])

    db_item = crud.create_item(item_name, item_cost, item_description, item_img, farm_name, category_name)
    items_in_db.append(db_item)


"""Categories"""
categories_in_db = []
for category in category_data:
    category_name = category['category_name']

    db_category = crud.create_category(category_name)
    categories_in_db.append(db_category)


"""Payment Methods"""
payment_methods_in_db = []
for payment_method in payment_data:
    payment_method_type = payment_method['payment_method_type']

    db_payment_method = crud.create_payment_method(payment_method_type)
    payment_methods_in_db.append(db_payment_method)


"""Pickup Locations"""
pickup_locations_in_db = []
for pickup_location in pickup_location_data:
    location_name, location_address, neighborhood_name = (pickup_location['location_name'],
                                        pickup_location['location_address'],
                                        pickup_location['neighborhood_name'])

    db_pickup_location = crud.create_pickup_location(location_name, location_address, neighborhood_name)
    pickup_locations_in_db.append(db_pickup_location)


"""Create 10 test users"""
for n in range(1, 10):
        email = f'user{n}@test.com'
        password = 'test'
        fname = 'test'
        lname = 'testerson'
        username = f'testy{n}'

        user = crud.create_user(email, password, fname, lname, username)


"""Creator login."""
c_email = 'leah@test.test'
c_password = 'test'
c_fname = 'Leah'
c_lname = 'Ewing'
c_username = 'leahnidus'

creator = crud.create_user(c_email, c_password, c_fname, c_lname, c_username)

