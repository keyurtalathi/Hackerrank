from flask import request,current_app as app
from questionanswer.conf.resource import BaseResource
from questionanswer.core.user_context import get_user_context
from questionanswer.models.add_testcase_handler import post_handler,get_handler
from questionanswer.core.make_database_connection import connect_to_geecoder
from questionanswer.views import testcase as testcaseView


class Testcase(BaseResource):
    def get(self):
        app.logger.info("in question get")
        params = request.args.to_dict()
        headers = request.headers
        response = get_handler(params)
        if response:
            return response, 200

    def post(self):
        app.logger.info("in question post")
        payload = request.json
        user_context = get_user_context()
        db, cursor = connect_to_geecoder()
        res = post_handle(payload, user_context, cursor)
        if res:
            res = testcaseView.single(res)
        db.commit()
        db.close()
        cursor.close()
        return res
