import webapp2
from google.appengine.api import users
from meetup.models import User
from webapp2_extras import jinja2


class BaseHandler(webapp2.RequestHandler):

    def __init__(self, *args, **kwargs):
        super(BaseHandler, self).__init__(*args, **kwargs)
        self.context = {}

    @property
    def email(self):
        return self.user.email()

    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

    def render(self, template):
        self.response.write(self.jinja2.render_template(template, **self.context))

    def urlFor(self, name, **kwargs):
        """
        get url by name
        :param name: name of URL
        :return: url
        """
        return webapp2.uri_for(name, self, **kwargs)

    @property
    def user(self):
        if not hasattr(self, '_user'):
            self._user = users.get_current_user()
        return self._user

    def confirm_user(self):
        user = User.get_by_id(self.email)
        if not user:
            User(email=self.email).put()
