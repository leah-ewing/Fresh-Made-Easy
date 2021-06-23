'use strict';


// list of all pickup locations in 'all-pickup-locations.html' //
$.get('/static/pickup-locations.json', (res) => {
    for (const pickup of res) {
        $('#pickup-location-file').append(`<ol><a id = "location-info" href = "/pickup-location-info/${pickup.location_name}">${pickup.location_name}</ol>`);
    }
});

// list of all farms in 'all-farms.html' //
$.get('/static/farms.json', (res) => {
    for (const farm of res) {
        $('#farm-file').append(`<ol><form action = "/farm-info/${farm.farm_name}" id = "farms"><a id = "farm-info" href = "/farm-info/${farm.farm_name}">${farm.farm_name}</a></form></ol>`);
    }
});

// list of all items in 'shop.html' with names and images //
$.get('/static/items.json', (res) => {
    for (const item of res) {
        $('#item-file').append(`<ol>
                                    <form action = "/item-info/${item.item_name}" id = "items">
                                        <a id = "item-info" href = "/item-info/${item.item_name}">
                                            <img class = "item-image"
                                                src = ${item.item_img}
                                                width = 200
                                                alt = "${item.item_name} image"> 
                                            </img>
                                            <br> ${item.item_name}
                                        </a>
                                        <br>
                                        <br>
                                    </form>
                                </ol>`);
    }
});

// list of all item categories in 'shop.html' //
$.get('/static/item-categories.json', (res) => {
    for (const category of res) {
        $("#category-list").append(`<ol><a id = "category-info" href = "/category-info/${category.category_name}">${category.category_name}</ol>`)
    }
});

// list of all farms in 'shop.html' //
$.get('/static/farms.json', (res) => {
    for (const farm of res) {
        $('#farm-list').append(`<ol><form action = "/farm-info/${farm.farm_name}" id = "farms"><a id = "farm-info" href = "/farm-info/${farm.farm_name}">${farm.farm_name}</a></form></ol>`);
    }
});


// $.get('static/items.json', (res) => {
//     for (const item of res) {
//         $.get('static/item-categories.json', (result) => {
//             for (const category of result) {
//                 if (item.category_name === category.category_name) {
//                     $('#category-item-list').append(`<ol><a id = "category-items" href = "/item-info/${item.item_name}`)
//                 }
//             }
//         })
//     }
// })

// $.get('/static/items.json', (res) => {
//     for (const item of res) {
//         $('#category-item-list').append(`<ol>
//                                     <form action = "/item-info/${item.item_name}" id = "items">
//                                         <a id = "item-info" href = "/item-info/${item.item_name}">
//                                             <img class = "item-image"
//                                                 src = ${item.item_img}
//                                                 width = 200
//                                                 alt = "${item.item_name} image"> 
//                                             </img>
//                                             <br> ${item.item_name}
//                                         </a>
//                                         <br>
//                                         <br>
//                                     </form>
//                                 </ol>`);
//     }
// });


// should be appending a list of items to the category-item-list -- not working right now.
$.get('/static/items.json', (res) => {
    for (const item of res) {
        $('#category-item-list').append(`${item.item_name}`);
    }
});