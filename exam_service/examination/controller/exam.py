from flask import request,current_app as app
from examination.conf.resource import BaseResource
from examination.models.exam_handler import post_handler,get_handler
from examination.core.make_database_connection import connect_to_geecoder
from examination.views import exam as examview


class Exam(BaseResource):
    def get(self, exam_id=None):
        app.logger.info("in exam get")
        db, cursor = connect_to_geecoder()
        res = get_handler(exam_id,cursor)
        db.commit()
        db.close()
        cursor.close()
        return res

    def post(self):
        app.logger.info("in exam post")
        payload = request.json
        db, cursor = connect_to_geecoder()
        res = post_handler(payload,cursor)
        if res:
            res = examview.single(res)
        db.commit()
        db.close()
        cursor.close()
        return res
