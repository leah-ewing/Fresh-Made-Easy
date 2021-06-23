
const nashville_coords = {
    lat: 36.1627,
    lng: -86.7816
  };
  

// ******* ATTEMPT ONE ********
// ******* refers to existing map "location-map" ******
// ******* currently shows map but doesn't show markers ******

  // const locationMap = google.maps.Map(
  //   document.querySelector('#location-map'),
  //   {
  //     center: nashville_coords,
  //     zoom: 11
  //   }
  // );

// ****** ATTEMPT ONE *********


// ****** ATTEMPT TWO *********
// ****** creates new map in div "location-map" ******
// ****** currently doesn't show maps or markers ******

// const locationMap = new google.maps.Map(document.querySelector("#location-map"),
//     {
//         center: nashville_coords,
//         zoom: 11
//     }
// );

// ****** ATTEMPT TWO *********


// ****** ATTEMPT THREE *********
// ****** refers to already-existing map "location-map" ******
// ****** doesn't change the way the map reacts for attempt 1 or 2 *******

// const locationMap = document.querySelector("#location-map"), {
//     center: nashville_coords
// }

// ****** ATTEMPT THREE *********


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
