'use strict';

// list of all items available from a farm on 'farm-info.html' //
// *** currently showing repeating items *** //
const currentFarm = document.getElementById("farm-info-name").innerText

$.get("/static/farms.json", (res) => {
    $.get("/static/items.json", (result) => {
        for (const farm of res) {
            for (const item of result) {
                if (item.farm_name == currentFarm) {
                    $("#farm-item-list").append(`<ol><form action = "/item-info/${item.item_name}" id = "farms-items"><a id = "farm-item-list-info" href = "/item-info/${item.item_name}"><img class = "item-image"
                                                                                                                                                                                            src = ${item.item_img}
                                                                                                                                                                                            width = 200
                                                                                                                                                                                            alt = "${item.item_name} image"> 
                                                                                                                                                                                        </img><br>${item.item_name}</a></form></ol>`)
                }
            }
        }
    })
});