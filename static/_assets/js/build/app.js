/* App.js */
"use strict";
'use strict';

/* App.js */

window.Home = {};

Home.componentForm = {
  street_number: 'short_name',
  route: 'long_name',
  locality: 'long_name',
  administrative_area_level_1: 'short_name',
  country: 'long_name',
  postal_code: 'short_name'
};

Home.autocomplete = function () {
  // Create the autocomplete object, restricting the search to geographical
  // location types.
  Home.gmapsAddress = new google.maps.places.Autocomplete(
  /** @type {!HTMLInputElement} */document.getElementById('address'), { types: ['geocode'] });

  // When the user selects an address from the dropdown, populate the address
  // fields in the form.
  // Home.gmapsAddress.addListener('place_changed', Home.fillInAddress);
};

Home.interests = function () {
  var checks = document.querySelectorAll('.check-list.interests .mdl-checkbox__input');

  Array.prototype.forEach.call(checks, function (check) {
    check.addEventListener('change', Home.interestsChangeHandler);
  });
};

Home.interestsChangeHandler = function (e) {
  var checked = document.querySelectorAll('.check-list.interests .mdl-checkbox__input:checked');

  document.getElementById('interests').value = Array.from(checked, function (check) {
    return check.id.split('checkbox_')[1];
  }).join(',');
};

Home.success = function () {
  var frame = document.getElementById('submit__frame');
  var response = JSON.parse(frame.contentWindow.document.body.textContent);
  window.location.href = '/room/' + response['event_id'];
};

Home.init = function () {
  Home.autocomplete();
  Home.interests();
  document.getElementById('event_date').valueAsDate = new Date();
  document.getElementById('submit__frame').addEventListener('load', Home.success);
};
'use strict';

window.Room = {};

Room.init = function () {
  var map;
  var infowindow;
  var pyrmont = { lat: 40.720369, lng: -73.988236 };
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

    google.maps.event.addListener(marker, 'click', function () {
      infowindow.setContent(place.name);
      infowindow.open(map, this);
    });
  };

  function updateCards(index, data) {
    var background = cards[index].querySelector('.mdl-card--expand');
    var title = cards[index].querySelector('.mdl-card__title-text');
    var desc = cards[index].querySelector('.mdl-card__supporting-text');

    background.style.backgroundImage = 'url(' + data.photos[0].getUrl({ 'maxWidth': 900, 'maxHeight': 600 }) + ')';
    title.textContent = data.name;
    desc.textContent = data.vicinity;
  };
};