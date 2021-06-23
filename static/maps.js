const nashville_coords = {
  lat: 36.1627,
  lng: -86.7816
};

// map on 'all-farms.html' //

function initFarmMap() {
  const farmMap = new google.maps.Map(document.querySelector("#farm-map"),
    {
        center: nashville_coords,
        zoom: 11
    }
);
  console.log("farm-map")
    const farms = [
      {
        name: "Gifford's Bacon",
        address: "1109 Straightway Ave, Nashville, TN 37206",
        coords: {
          lat: 36.174080,
          lng: -86.759710
          //change these lat/longs
        }
      },
      {
        name: "Porter Road Butcher",
        address: "501 Gallatin Ave, Nashville, Tennessee 37206",
        coords: {
          lat: 36.157028,
          lng: -86.839241
        }
      },
      {
        name: "Johnson's Honey Farm",
        address: "1206 South, Dickerson Rd, Goodlettsville, TN 37072",
        coords: {
          lat: 36.190350,
          lng: -86.680153
        }
      },
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
  
      marker.addListener('mouseover', () => {
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
  
      marker.addListener('mouseover', () => {
        infoWindow.open(locationMap, marker);
      });
    }
  }
