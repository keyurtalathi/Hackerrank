from flask import request,current_app as app
from questionanswer.conf.resource import BaseResource
from questionanswer.models.run_program import post_handler
from questionanswer.core.make_database_connection import connect_to_geecoder


class Run(BaseResource):

    def post(self):
        app.logger.info("in add subtopic post")
        payload = request.json
        db, cursor = connect_to_geecoder()
        res = post_handler(payload, cursor)
        db.close()
        cursor.close()
        return res
