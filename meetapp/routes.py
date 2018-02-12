import handlers
import webapp2


app = webapp2.WSGIApplication([
    webapp2.Route('/', handler=handlers.HomeHandler),
    webapp2.Route('/room/<room_id:(.*)>', handler=handlers.RoomHandler),
    webapp2.Route(handlers.OAUTH_DECORATOR.callback_path, handler=handlers.OAUTH_DECORATOR.callback_handler()),
])
