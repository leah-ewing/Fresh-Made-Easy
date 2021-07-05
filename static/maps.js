const nashville_coords = {
  lat: 36.1627,
  lng: -86.7816
};

// map on 'all-farms.html' //
function initFarmMap() {
  const farmMap = new google.maps.Map(document.querySelector("#farm-map"),
    {
        center: nashville_coords,
        zoom: 7
    }
);
  console.log("farm-map")
    const farms = [
      {
        name: "Gifford's Bacon",
        address: "1109 Straightway Ave, Nashville, TN 37206",
        coords: {
          lat: 36.193920,
          lng: -86.742370
        }
      },
      {
        name: "Porter Road Butcher",
        address: "501 Gallatin Ave, Nashville, Tennessee 37206",
        coords: {
          lat: 36.181910,
          lng: -86.748920
        }
      },
      {
        name: "Johnson's Honey Farm",
        address: "1206 South, Dickerson Rd, Goodlettsville, TN 37072",
        coords: {
          lat: 36.292910,
          lng: -86.728580
        } 
      },
      {
        name: "Sequatchie Cove Creamery",
        address: "2216 Coppinger Cove Rd, Sequatchie, TN 37374",
        coords: {
          lat: 35.151890,
          lng: -85.603073
        }
      },
      {
        name: "Hatcher Family Dairy",
        address: "6545 Arno Road College Grove, TN 37046",
        coords: {
          lat: 35.81621,
          lng: -86.73609
        }
      },
      {
        name: "Annie Acres",
        address: "4610 Eatons Creek Road, Nashville, TN 37218",
        coords: {
          lat: 36.22987,
          lng: -86.86841
        }
      }, 
      {
        name: "Pure Pasture Farms",
        address: "900 Rosa L Parks Blvd, Nashville, TN 37208",
        coords: {
          lat: 36.188476,
          lng: -86.708395,
        }
      },
      {
        name: "Tennessee Grassfed",
        address: "335 Williams Rd, Clarksville, TN 37043",
        coords: {
          lat: 36.45447,
          lng: -87.14819,
        }
      },
      {
        name: "GooGoo Cluster",
        address: "116 3rd Ave S, Nashville, TN 37201",
        coords: {
          lat: 36.16089,
          lng: -86.77552,
        }
      }
    ];
  
    const markers = [];
    for (const farm of farms) {
      markers.push(new google.maps.Marker({
        position: farm.coords,
        title: farm.name,
        address: farm.address,
        map: farmMap
      }));
    }
  
    for (const marker of markers) {
      const markerInfo = (`
        <h1>${marker.title}</h1>
        <p>
          <code>${marker.address}</code>
        </p>
      `);
  
      const infoWindow = new google.maps.InfoWindow({
        content: markerInfo,
        maxWidth: 200
      });
  
      marker.addListener('click', () => {
        infoWindow.open(farmMap, marker);
      });
    }
  }


// map on 'all-pickup-locations.html' // 
  function initLocationMap() {
  const locationMap = new google.maps.Map(document.querySelector("#location-map"),
    {
        center: nashville_coords,
        zoom: 11
    }
);
  console.log("location-map")
    const locations = [
      {
        name: "Turnip Truck",
        address: "701 Woodland St, Nashville, TN 37206",
        coords: {
          lat: 36.174080,
          lng: -86.759710
        }
      },
      {
        name: "Fat Bottom Brewing",
        address: "800 44th Ave N, Nashville, TN 37209",
        coords: {
          lat: 36.157028,
          lng: -86.839241
        }
      },
      {
        name: "Donelson Farmer's Market",
        address: "3130 McGavock Pk, Nashville, TN 37214",
        coords: {
          lat: 36.190350,
          lng: -86.680153
        }
      },
      {
        name: "Phat Bites",
        address: "2730 Lebanon Pike B, Nashville, TN 37214",
        coords: {
          lat: 36.1684,
          lng: -86.66591
        }
      },
      {
        name: "Prime South Meats",
        address: "1109 Straightway Ave, Nashville, TN 37206",
        coords: {
          lat: 36.19352,
          lng: -86.74241
        }
      },
      {
        name: "Hendersonville Produce",
        address: "760 E Main St, Hendersonville, TN 37075",
        coords: {
          lat: 36.32643,
          lng: -86.56297
        }
      },
      {
        name: "Almustafa Market",
        address: "943 Richards Rd, Antioch, TN 37013",
        coords: {
          lat: 36.0691,
          lng: -86.68235
        }
      },
      {
        name: "Mari Supermercado",
        address: "4000 Lebanon Pike, Hermitage, TN 37076",
        coords: {
          lat: 36.19592,
          lng: -86.62153
        }
      },
      {
        name: "The Produce Place",
        address: "4000 Murphy Rd, Nashville, TN 37209",
        coords: {
          lat: 36.14074,
          lng: -86.83332
        }
      },
      {
        name: "Urban Roots Market",
        address: "1307 2nd Ave N, Nashville, TN 37208",
        coords: {
          lat: 36.14162,
          lng: -86.76201
        }
      },
      {
        name: "Savi Urban Market",
        address: "415 Church St, Nashville, TN 37219",
        coords: {
          lat: 36.16344,
          lng: -86.77957
        }
      },
      {
        name: "Sinema",
        address: "2600 8th Ave S Suite 102, Nashville, TN 37204",
        coords: {
          lat: 36.12196,
          lng: -86.77561
        }
      },
      {
        name: "Five Daughter's Bakery",
        address: "1110 Caruthers Ave, Nashville, TN 37204",
        coords: {
          lat: 36.12574,
          lng: -86.78842
        }
      }
    ];
  
    const markers = [];
    for (const location of locations) {
      markers.push(new google.maps.Marker({
        position: location.coords,
        title: location.name,
        address: location.address,
        map: locationMap
      }));
    }
  
    for (const marker of markers) {
      const markerInfo = (`
        <h1>${marker.title}</h1>
        <p>
          <code>${marker.address}</code>
        </p>
      `);
  
      const infoWindow = new google.maps.InfoWindow({
        content: markerInfo,
        maxWidth: 200
      });
  
      marker.addListener('click', () => {
        infoWindow.open(locationMap, marker);
      });
    }
  }
