from flask import request,current_app as app
from questionanswer.conf.resource import BaseResource
from questionanswer.core.user_context import get_user_context
from questionanswer.models.add_question_handler import post_handler,get_handler
from questionanswer.core.make_database_connection import connect_to_geecoder
from questionanswer.views import question as questionView


class Question(BaseResource):
    def get(self, question_id=None, sub_topic_id=None):
        app.logger.info("IN QUESTION GET")
        params = request.args.to_dict()
        if "question_id" in params:
            question_id = params["question_id"]
        if "sub_topic_id" in params:
            sub_topic_id = params["sub_topic_id"]
        #headers = request.headers
        response = get_handler(question_id, sub_topic_id)
        if response:
            return response

    def post(self):
        app.logger.info("in question post")
        payload = request.json
        user_context = get_user_context()
        db, cursor = connect_to_geecoder()
        res = post_handler(payload, user_context, cursor)
        if res:
            res = questionView.single(res)
        db.commit()
        db.close()
        cursor.close()
        return res
