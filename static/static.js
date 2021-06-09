'use strict';


$.get('/static/pickup-locations.json', (res) => {
    for (const pickup of res) {
        $('#pickup-location-api').append(`<li>${pickup.location_name}</li>`);
    }
});