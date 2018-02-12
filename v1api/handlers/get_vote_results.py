from base import BaseApiV1Handler


class GetVoteResultsHandler(BaseApiV1Handler):

    def results(self):
        return dict(
            status='incomplete',
        )
