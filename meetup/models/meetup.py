import uuid
from google.appengine.ext import ndb
from utils import GeoCoding


class Meetup(ndb.Model):
    creator = ndb.StringProperty(required=True) # email
    title = ndb.StringProperty(required=True)
    time = ndb.DateTimeProperty(required=True)
    moods = ndb.StringProperty(repeated=True)
    interests = ndb.StringProperty(repeated=True)
    count = ndb.IntegerProperty(required=True)
    # auto fields
    created = ndb.DateTimeProperty(auto_now_add=True)
    modified = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def _generate_key(cls):
        return ndb.Key(cls, unicode(uuid.uuid4()))

    def _pre_put_hook(self):
        if not self.key.id():
            self.key = self._generate_key()

    def midpoint(self, user_meetups):
        locations = [u.location for u in user_meetups if u.location]
        if locations:
            lat = [l.lat for l in locations]
            lng = [l.lon for l in locations]
            lat = sum(lat) / len(lat)
            lng = sum(lng) / len(lng)
            return dict(lat=lat, lng=lng)


class UserMeetup(ndb.Model):
    email = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=False)
    meetup = ndb.KeyProperty(Meetup, required=True)
    address = ndb.StringProperty(required=False)
    location = ndb.GeoPtProperty(required=False)
    moods = ndb.StringProperty(repeated=True)
    interests = ndb.StringProperty(repeated=True)
    statuses = ndb.StringProperty(repeated=True)
    vote = ndb.JsonProperty(required=False)
    # auto fields
    created = ndb.DateTimeProperty(auto_now_add=True)
    modified = ndb.DateTimeProperty(auto_now=True)

    def _pre_put_hook(self):
        if 'preferences' not in self.statuses:
            if self.address and self.moods and self.interests:
                self.statuses.append('preferences')
        if 'vote' not in self.statuses:
            if self.vote:
                self.statuses.append('vote')
        if self.address and not self.location:
            response = GeoCoding.get_location(address=self.address)
            location = response['results'][0]['geometry']['location']
            lat = location['lat']
            lng = location['lng']
            self.location = ndb.GeoPt(lat=lat, lon=lng) # lat, lon
