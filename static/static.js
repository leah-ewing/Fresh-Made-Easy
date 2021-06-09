'use strict';

// list of all pickup locations in 'all-pickup-locations.html'
$.get('/static/pickup-locations.json', (res) => {
    for (const pickup of res) {
        $('#pickup-location-api').append(`<ol><a href = '/pickup-location-info'>${pickup.location_name}</ol>`);
    }
});
// links right now aren't going anywhere, make a route in server.py

// list of all farms in 'all-farms.html'
$.get('/static/farms.json', (res) => {
    for (const farm of res) {
        $('#farm-api').append(`<ol><a href = '/farm-info'>${farm.farm_name}</a></ol>`);
    }
});
// links right now aren't going anywhere, make a route in server.py