class BaseConfig(object):
    SITE_URL = 'http://127.0.0.1:8000/'
    CORS_ALLOW_HEADERS = ['Origin', 'Content-Type',
                          'Accept', 'X-Authorization-Token']
    CORS_ALLOW_ORIGINS = ['*']
    CORS_ALLOW_METHODS = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']
    USER_SERVICE_URL = "http://0.0.0.0:7281/"
