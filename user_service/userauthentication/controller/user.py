from userauthentication.conf.resource import BaseResource
from flask import request, current_app as app
from userauthentication.models.user_handler import get_user_handler, post_user_handler
from userauthentication.exceptions.unauthorised_exception import UnauthorisedException
from userauthentication.exceptions.bad_request import BadRequest


class User(BaseResource):

    def get(self, user_id=None):
        app.logger.info("in user get")
        try:
            headers = request.headers
            response = get_user_handler(headers, user_id)
            if response:
                return response, 200
            raise UnauthorisedException
        except:
            raise BadRequest

    def post(self):
        payload = request.json
        response = post_user_handler(payload)
        return response
