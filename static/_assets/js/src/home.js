/* App.js */

window.Home = {};

Home.componentForm = {
  street_number: 'short_name',
  route: 'long_name',
  locality: 'long_name',
  administrative_area_level_1: 'short_name',
  country: 'long_name',
  postal_code: 'short_name'
}

Home.autocomplete = function() {
  // Create the autocomplete object, restricting the search to geographical
  // location types.
  Home.gmapsAddress = new google.maps.places.Autocomplete(
    /** @type {!HTMLInputElement} */(document.getElementById('address')),
    {types: ['geocode']});

  // When the user selects an address from the dropdown, populate the address
  // fields in the form.
  // Home.gmapsAddress.addListener('place_changed', Home.fillInAddress);
}

Home.interests = function() {
  const checks = document.querySelectorAll('.check-list.interests .mdl-checkbox__input');

  Array.prototype.forEach.call(checks, check => {
    check.addEventListener('change', Home.interestsChangeHandler);
  });
}

Home.interestsChangeHandler = function(e) {
  const checked = document.querySelectorAll('.check-list.interests .mdl-checkbox__input:checked');

  document.getElementById('interests').value = Array.from(checked, check => check.id.split('checkbox_')[1]).join(',');
}

Home.success = function() {
  const frame = document.getElementById('submit__frame');
  const response = JSON.parse( frame.contentWindow.document.body.textContent );
  window.location.href = `/room/${response['event_id']}`;
}

Home.init = function() {
  Home.autocomplete();
  Home.interests();
  document.getElementById('event_date').valueAsDate = new Date();
  document.getElementById('submit__frame').addEventListener('load', Home.success);
}
