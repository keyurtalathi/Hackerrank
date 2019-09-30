try:
    import cPickle as pickle
except ImportError:
    import pickle
import uuid
from flask.sessions import SessionInterface, SessionMixin
from apigateway.clients.user_service_client import get_active_user
from werkzeug.datastructures import CallbackDict


class UserServiceSession(CallbackDict, SessionMixin):
    def __init__(self, initial=None, user_id=None, username=None, groups=None,
                 last_login=None):
        def on_update(self):
            self.modified = True

        CallbackDict.__init__(self, initial, on_update)
        self.user_id = user_id
        self.username = username
        self.groups = groups
        self.last_login = last_login
        self.modified = False


#
class UserServiceInterface(SessionInterface):
    #     pickle_based = False
    session_class = UserServiceSession

    def open_session(self, app, request):
        # print "i am in open session"
        key = request.cookies.get(app.session_cookie_name,
                                  request.headers.get(app.auth_header_name))

        print key
        print '<===============================>'
        session = None
        if key:
            response_data = get_active_user(token=key, app=app)
        else:
            response_data = None
        print "=== User apigateway response." , response_data
        if not response_data:
            app.logger.info("fatal no session info from user apigateway")
            session = self.session_class()
            session['key'] = key = str(uuid.uuid4())
        else:
            print response_data
            response_data["key"] = key
            session = self.session_class(response_data)
            session["key"] = key
            session["username"] = response_data["emailId"]
            session["groups"] = response_data["groups"]
            session["last_name"] = response_data["lastName"]
            session["first_name"] = response_data["firstName"]
            session["user_id"] = response_data["id"]
        # print "Done with session"
        return session


    def save_session(self, app, session, response):
        domain = self.get_cookie_domain(app)
        path = self.get_cookie_path(app)
        httponly = self.get_cookie_httponly(app)
        secure = self.get_cookie_secure(app)
        expires = self.get_expiration_time(app, session)
