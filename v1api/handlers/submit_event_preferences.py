from base import BaseApiV1Handler
from meetup.models import UserMeetup, Meetup


class SubmitEventPreferencesHandler(BaseApiV1Handler):

    def get(self):
        self.response.write("""
        <form method='POST'>
            event_id: <input type="text" name="event_id"><br>
            name: <input type="text" name="title"><br>
            address: <input type="text" name="address"><br>
            interests (,): <input type="text" name="interests"><br>
            moods (,): <input type="text" name="moods"><br>
            <button type="submit">Submit</button>
        </form>
        """)

    def post(self):
        event_id = self.request.POST['event_id']
        name = self.request.POST.get('name')
        address = self.request.POST.get('address')

        interests = self.request.POST.get('interests')
        if interests: interests = interests.split(',')
        moods = self.request.POST.get('moods')
        if moods: moods = moods.split(',')

        meetup = Meetup.get_by_id(event_id)
        um = UserMeetup.query(UserMeetup.meetup==meetup.key, UserMeetup.email==self.email).get()
        if not um:
            um = UserMeetup(
                email=self.email,
                meetup=meetup.key,
            )

        if name:
            um.name = name
        if address:
            um.address = address
        if moods:
            um.moods = moods
        if interests:
            um.interests = interests

        um.put()

        self.out(dict(status='ok'))
