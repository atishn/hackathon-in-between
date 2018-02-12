import handlers
import webapp2


app = webapp2.WSGIApplication([
    webapp2.Route('/api/v1/create-event', handler=handlers.CreateEventHandler),
    webapp2.Route('/api/v1/event-status', handler=handlers.EventStatusHandler),
    webapp2.Route('/api/v1/get-event-setup', handler=handlers.GetEventSetupHandler),
    webapp2.Route('/api/v1/get-event-suggestions', handler=handlers.GetEventSuggestionsHandler),
    webapp2.Route('/api/v1/get-vote-results', handler=handlers.GetVoteResultsHandler),
    webapp2.Route('/api/v1/submit-event-preferences', handler=handlers.SubmitEventPreferencesHandler),
    webapp2.Route('/api/v1/vote-event-suggestions', handler=handlers.VoteEventSuggestionsHandler),
])
