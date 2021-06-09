'use strict';


$.get('/static/pickup-locations.json', (res) => {
    for (const pickup of res) {
        $('#pickup-location-api').append(`<li>${pickup.location_name}</li>`);
    }
});

$.get('/static/farms.json', (res) => {
    for (const farm of res) {
        $('#farm-api').append(`<li>${farm.farm_name}</li>`);
    }
});