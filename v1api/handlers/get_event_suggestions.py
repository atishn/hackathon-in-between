from base import BaseApiV1Handler


class GetEventSuggestionsHandler(BaseApiV1Handler):

    def results(self):
        return dict(
            suggestion='get a life',
        )
