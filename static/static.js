'use strict';


// list of all pickup locations in 'all-pickup-locations.html'
$.get('/static/pickup-locations.json', (res) => {
    for (const pickup of res) {
        $('#pickup-location-api').append(`<ol><a href = '/pickup-location-info'>${pickup.location_name}</ol>`);
    }
});

// list of all farms in 'all-farms.html'
$.get('/static/farms.json', (res) => {
    for (const farm of res) {
        $('#farm-api').append(`<ol><a href = '/farm-info'>${farm.farm_name}</a></ol>`);
    }
});

// list of all items in 'shop.html' with names and images
$.get('/static/items.json', (res) => {
    for (const item of res) {
        $('#item-api').append(`<ol><a id = "item-info" href = '/item-info'><img class = "item-image"
                                    src = ${item.item_img}
                                    width = 200
                                    alt = "${item.item_name} image"</img><br>
                                    ${item.item_name}</a><br><br></ol>`);

               
        $('#name-item').append(`${item.item_name}`)
        $('#description-item').append(`${item.item_description}`)
        $('#price-item').append(`${item.item_cost}`)
    }
});
