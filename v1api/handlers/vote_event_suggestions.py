from base import BaseApiV1Handler


class VoteEventSuggestionsHandler(BaseApiV1Handler):

    def results(self):
        return dict(
            status='not done',
        )
