from flask import request,current_app as app
from questionanswer.conf.resource import BaseResource
from questionanswer.core.user_context import get_user_context
from questionanswer.models.add_sub_topic_handler import post_handler,get_handler
from questionanswer.core.make_database_connection import connect_to_geecoder
from questionanswer.views import sub_topic as subtopicview


class SubTopic(BaseResource):
    def get(self, sub_topic_id=None, topic_id= None):
        app.logger.info("in sub_topic get")
        params = request.args.to_dict()
        if "sub_topic_id" in params:
            sub_topic_id = params["sub_topic_id"]
        if "topic_id" in params:
            topic_id = params["topic_id"]
        response = get_handler(sub_topic_id, topic_id)
        if response:
            return response

    def post(self):
        app.logger.info("in add subtopic post")
        payload = request.json
        user_context = get_user_context()
        db, cursor = connect_to_geecoder()
        res = post_handler(payload, user_context, cursor)
        if res:
            res = subtopicview.single(res)
        db.commit()
        db.close()
        cursor.close()
        return res
