import json
import urllib
from google.appengine.api import urlfetch


API_KEY = 'AIzaSyDzdJug9qiXpGG2Z3iVsYx9pjX75P2k9xI'
URL = 'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={key}'


class GeoCoding(object):

    @classmethod
    def get_location(cls, address):
        urlfetch.set_default_fetch_deadline(30)
        response = urlfetch.fetch(
            URL.format(key=API_KEY, address=urllib.quote_plus(address)),
            method=urlfetch.GET,
        )
        if response.status_code == 200:
            return json.loads(response.content)
