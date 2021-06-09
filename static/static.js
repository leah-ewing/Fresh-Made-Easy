'use strict';


$.get('pickup-locations.json', (res) => {
    for (const pickupLocation of res.results) {
        $('#pickup-location-api').append(`<li>${pickupLocation.locaton_name}</li>`);
    }
});