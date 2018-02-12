from base import BaseApiV1Handler
from meetup.models import Meetup, UserMeetup


class EventStatusHandler(BaseApiV1Handler):

    def get(self):
        id = self.request.GET['event_id']
        meetup = Meetup.get_by_id(id)
        users = UserMeetup.query(UserMeetup.meetup==meetup.key)

        self.out(dict(
            creator=meetup.creator,
            title=meetup.title,
            event_date=meetup.time.isoformat(),
            moods=meetup.moods,
            interests=meetup.interests,
            count=meetup.count,
            crated=meetup.created.isoformat(),
            midpoint=meetup.midpoint(user_meetups=users),
            users=[
                dict(
                    email=u.email,
                    name=u.name,
                    address=u.address,
                    moods=u.moods,
                    interests=u.interests,
                    statuses=u.statuses,
                    location=dict(
                        lat=u.location.lat,
                        lng=u.location.lon,
                    ) if u.location else None,
                )
            for u in users]
        ))
