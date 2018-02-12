from google.appengine.ext import ndb


class User(ndb.Model):
    email = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=False)
    # auto fields
    created = ndb.DateTimeProperty(auto_now_add=True)
    modified = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def _generate_key(cls, email):
        return ndb.Key(cls, email)

    def _pre_put_hook(self):
        if not self.key.id():
            self.key = self._generate_key(email=self.email)
