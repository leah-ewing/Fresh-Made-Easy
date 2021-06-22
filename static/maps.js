const  pickupLocationCoords = {
    lat: 36.1627,
    lng: -86.7816
  };
  
  const basicMap = new google.maps.Map(
    document.querySelector('#location-map'),
    {
      center: pickupLocationCoords,
      zoom: 11
    }
  );

function initLocationMap() {
    const locations = [
      {
        name: "Turnip Truck",
        coords: {
          lat: 36.174080,
          lng: -86.759710
        }
      },
      {
        name: "Fat Bottom Brewing",
        coords: {
          lat: 36.157028,
          lng: -86.839241
        }
      },
      {
        name: "Donelson Farmer's Market",
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
        map: basicMap
      }));
    }
  
    for (const marker of markers) {
      const markerInfo = (`
        <h1>${marker.title}</h1>
        <p>
          Located at: <code>${marker.position.lat()}</code>,
          <code>${marker.position.lng()}</code>
        </p>
      `);
  
      const infoWindow = new google.maps.InfoWindow({
        content: markerInfo,
        maxWidth: 200
      });
  
      marker.addListener('click', () => {
        infoWindow.open(basicMap, marker);
      });
    }
  }
