from datetime import datetime
from userauthentication.conf.resource import BaseResource
from flask import request
import uuid
from userauthentication.dao.user import get_user_by_mail
from userauthentication.dao.session import create_user_session
from userauthentication.exceptions.not_found_exception import NotFoundException
from userauthentication.exceptions.bad_request import BadRequest
from userauthentication.exceptions.unauthorised_exception import \
    UnauthorisedException
from userauthentication.core.make_database_connection import connect_to_geecoder
from userauthentication.utils.datetime_utils import datetime_to_utcms


class UserValidation(BaseResource):
    def post(self):
        payload = request.json
        db, cursor = connect_to_geecoder()
        try:
            email = payload['email']
            password = payload['password']
        except:
            raise BadRequest

        user = get_user_by_mail(email, cursor)
        if not user:
            raise NotFoundException

        if not user["password"] == password:
            raise UnauthorisedException

        token = str(uuid.uuid4())
        expiry = datetime.now()
        expiry = datetime_to_utcms(expiry, months_delta=12, days_delta=31)
        create_user_session(user["id"], token, cursor, expiry)
        db.commit()
        cursor.close()
        db.close()
        return {
                "X-Authorization-Token": token,
                "expiry": expiry
            }
