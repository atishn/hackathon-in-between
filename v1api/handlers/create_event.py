import datetime
from base import BaseApiV1Handler
from meetup.models import Meetup, UserMeetup


class CreateEventHandler(BaseApiV1Handler):

    def get_event_date(self):
        date = self.request.POST['event_date']
        date = date.replace('T', '-').replace(':', '-').split('-')
        date = [int(v) for v in date]
        return datetime.datetime(*date)

    def post(self):
        title = self.request.POST['title']
        count = int(self.request.POST['count'])
        address = self.request.POST.get('address')
        name = self.request.POST.get('name')
        event_date = self.get_event_date()

        interests = self.request.POST.get('interests')
        if interests: interests = interests.split(',')
        moods = self.request.POST.get('moods')
        if moods: moods = moods.split(',')

        meetup = Meetup(
            creator=self.email,
            title=title,
            time=event_date,
            moods=moods,
            interests=interests,
            count=count,
        )
        meetup.put()

        um = UserMeetup(
            name=name,
            email=self.email,
            meetup=meetup.key,
            address=address,
            moods=moods,
            interests=interests,
        )
        um.put()

        self.out(dict(
            event_id=meetup.key.id(),
        ))

    def results(self):
        return dict(
            count='number',
            address='',
            event_date='',
            interests='',
            moods=''
        )

    def get(self):
        self.response.write("""
        <form method='POST'>
            name: <input type="text" name="name"><br>
            title: <input type="text" name="title"><br>
            count: <input type="number" name="count"><br>
            address: <input type="text" name="address"><br>
            event_date: <input type="datetime-local" name="event_date"><br>
            interests (,): <input type="text" name="interests"><br>
            moods (,): <input type="text" name="moods"><br>
            <button type="submit">Submit</button>
        </form>
        """)
