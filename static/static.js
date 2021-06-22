'use strict';

// function initMap() {
//     const locations = [
//       {
//         name: "Turnip Truck",
//         coords: {
//           lat: 36.174080,
//           lng: -86.759710
//         }
//       },
//       {
//         name: "Fat Bottom Brewing",
//         coords: {
//           lat: 36.157028,
//           lng: --86.839241
//         }
//       },
//       {
//         name: "Donelson Farmer's Market",
//         coords: {
//           lat: 36.190350,
//           lng: -86.680153
//         }
//       },
//     ];
  
//     const markers = [];
//     for (const location of locations) {
//       markers.push(new google.maps.Marker({
//         position: location.coords,
//         title: location.name,
//         map: basicMap,
//         icon: {  // custom icon
//           url: '/static/img/marker.svg',
//           scaledSize: {
//             width: 30,
//             height: 30
//           }
//         }
//       }));
//     }
  
//     for (const marker of markers) {
//       const markerInfo = (`
//         <h1>${marker.title}</h1>
//         <p>
//           Located at: <code>${marker.position.lat()}</code>,
//           <code>${marker.position.lng()}</code>
//         </p>
//       `);
  
//       const infoWindow = new google.maps.InfoWindow({
//         content: markerInfo,
//         maxWidth: 200
//       });
  
//       marker.addListener('click', () => {
//         infoWindow.open(basicMap, marker);
//       });
//     }
//   }

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