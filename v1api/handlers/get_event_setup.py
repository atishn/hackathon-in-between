from base import BaseApiV1Handler


class GetEventSetupHandler(BaseApiV1Handler):

    def results(self):
        return dict(
            email=self.email,
            interests=['coffee', 'bar'],
            moods=['chill', 'happy'],
        )
