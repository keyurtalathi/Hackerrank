from flask import request,current_app as app
from questionanswer.conf.resource import BaseResource
from questionanswer.core.user_context import get_user_context
from questionanswer.models.add_topic_handler import post_handler,get_handler
from questionanswer.core.make_database_connection import connect_to_geecoder
from questionanswer.views import topic as topicview


class Topic(BaseResource):
    def get(self, topic_id=None):
        app.logger.info("in topic get")
        params = request.args.to_dict()
        if "topic_id" in params:
            topic_id = params["topic_id"]
        # headers = request.headers
        response = get_handler(topic_id)
        return response

    def post(self):
        app.logger.info("in addtopic post")
        payload = request.json
        user_context = get_user_context()
        db, cursor = connect_to_geecoder()
        res = post_handler(payload,user_context,cursor)
        if res:
            res = topicview.single(res)
        db.commit()
        db.close()
        cursor.close()
        return res
