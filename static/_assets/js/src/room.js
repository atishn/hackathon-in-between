window.Room = {};

Room.init = function() {
  var map;
  var infowindow;
  var pyrmont = {lat: 40.720369, lng: -73.988236};
  var cards = document.querySelectorAll('.demo-card-square');

  map = new google.maps.Map(document.getElementById('map'), {
    center: pyrmont,
    zoom: 15
  });

  infowindow = new google.maps.InfoWindow();
  var service = new google.maps.places.PlacesService(map);
  service.nearbySearch({
    location: pyrmont,
    radius: 500,
    type: ['bar']
  }, callback);

  function callback(results, status) {
    console.log(status, results);
    if (status === google.maps.places.PlacesServiceStatus.OK) {
      for (var i = 0; i < results.length; i++) {
        if (i < 6) {
          createMarker(results[i]);
          updateCards(i, results[i]);
        }
      }
    }
  }

  function createMarker(place) {
    var placeLoc = place.geometry.location;
    var marker = new google.maps.Marker({
      map: map,
      position: place.geometry.location
    });

    google.maps.event.addListener(marker, 'click', function() {
      infowindow.setContent(place.name);
      infowindow.open(map, this);
    });
  };

  function updateCards(index, data) {
    var background = cards[index].querySelector('.mdl-card--expand');
    var title = cards[index].querySelector('.mdl-card__title-text');
    var desc = cards[index].querySelector('.mdl-card__supporting-text');

    background.style.backgroundImage = 'url(' + data.photos[0].getUrl({'maxWidth': 900, 'maxHeight': 600}) +')';
    title.textContent = data.name;
    desc.textContent = data.vicinity;
  };
};


