'use strict';

// list of all items matching a chosen category on 'category-info.html' //
// currently showing all items *** //
const currentCategory = document.getElementById("category-info-name").innerText
console.log(currentCategory)

$.get("/static/item-categories.json", (res) => {
    $.get("/static/items.json", (result) => {
        for (const category of res) {
            for (const item of result) {
                if (item.category_name == currentCategory) {
                    $("#category-item-list").append(`<ol><form action = "/item-info/${item.item_name}" id = "farms-items"><a id = "farm-item-list-info" href = "/item-info/${item.item_name}"><img class = "item-image"
                                                                                                                                                                                                src = ${item.item_img}
                                                                                                                                                                                                width = 200
                                                                                                                                                                                                alt = "${item.item_name} image"> 
                                                                                                                                                                                            </img><br>${item.item_name}</a></form></ol>`)
                }
            }
        }
    })
});