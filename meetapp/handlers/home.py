from base import BaseHandler
from oauth2callback import OAUTH_DECORATOR


class HomeHandler(BaseHandler):

    @OAUTH_DECORATOR.oauth_required
    def get(self):
        self.confirm_user()
        self.render('pages/home.html')
