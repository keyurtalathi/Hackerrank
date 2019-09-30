from userauthentication.conf.resource import BaseResource
from flask import current_app as app, request
from userauthentication.exceptions.bad_request import BadRequest
from userauthentication.core.make_database_connection import connect_to_geecoder
from userauthentication.dao.role import create_role, get_latest_role


class Role(BaseResource):
    def post(self):
        app.logger.info("in role post")
        try:
            payload = request.json
            db, cursor = connect_to_geecoder()
            create_role(payload["role"], cursor)
            res = get_latest_role()
            db.commit()
            db.close()
            cursor.close()
            return res
        except:
            raise BadRequest