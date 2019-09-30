from userauthentication.conf.resource import BaseResource
from flask import current_app as app


class Ping(BaseResource):
    def get(self):
        app.logger.info("in ping get")
        return "All OK"