import logging
from base import BaseHandler
from meetup.models import Meetup, UserMeetup
from oauth2callback import OAUTH_DECORATOR


class RoomHandler(BaseHandler):

    @OAUTH_DECORATOR.oauth_required
    def get(self, room_id):
        self.confirm_user()
        meetup = Meetup.get_by_id(room_id)

        users = UserMeetup.query(UserMeetup.meetup==meetup.key).fetch()
        if self.email not in [u.email for u in users]:
            um = UserMeetup(
                email=self.email,
                meetup=meetup.key,
            )
            um.put()
            users.append(um)

        self.context = {
            'current_user': self.email,
            'room_id': room_id,
            'meetup': meetup,
            'users': users,
        }

        self.render('pages/room.html')
