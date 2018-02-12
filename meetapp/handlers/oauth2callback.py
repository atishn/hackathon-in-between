from oauth2client.contrib.appengine import OAuth2Decorator


OAUTH_DECORATOR = OAuth2Decorator(
    client_id='405427916132-5973brd7egkdsptqdck52992lvspvv0s.apps.googleusercontent.com',
    client_secret='sBgVwvA6caPGsb4vJY9mwROM',
    scope=[
        'https://www.googleapis.com/auth/userinfo.email',
    ],
    callback_path='/oauth2callback'
)
