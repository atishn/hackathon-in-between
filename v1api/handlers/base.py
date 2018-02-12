import json
import webapp2
from google.appengine.api import users
from meetup.models import User, Meetup


class BaseApiV1Handler(webapp2.RequestHandler):

    @property
    def email(self):
        return self.user.email()

    def results(self):
        raise NotImplementedError('Need to define a results function.')

    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(self.results()))

    def out(self, data):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(data))

    @property
    def user(self):
        if not hasattr(self, '_user'):

            self._user = users.get_current_user()
        return self._user

    @property
    def meet_user(self):
        if not hasattr(self, '_meet_user'):
            user = User.get_by_id(self.email)
            if not user:
                user = User(email=self.email)
                user.put()
            self._meet_user = user
        return self._meet_user

    def get_meetup(self, id):
        if not hasattr(self, '_get_meetup'):
            self._get_meetup = Meetup.get_by_id(id)
        return self._get_meetup
