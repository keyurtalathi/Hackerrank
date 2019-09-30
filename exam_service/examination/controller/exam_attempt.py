from flask import request,current_app as app
from examination.conf.resource import BaseResource
from examination.models.exam_attempt_handler import get_handler, post_handler
from examination.core.make_database_connection import connect_to_geecoder
from examination.views import exam_attempt as examattemptview


class ExamAttempt(BaseResource):
    def get(self, exam_attempt_id=None):
        app.logger.info("in examattempt get")
        db, cursor = connect_to_geecoder()
        res = get_handler(exam_attempt_id,cursor)
        db.commit()
        db.close()
        cursor.close()
        return res

    def post(self):
        app.logger.info("in examattempt post")
        payload = request.json
        db, cursor = connect_to_geecoder()
        res = post_handler(payload,cursor)
        if res:
            res = examattemptview.single(res)
        db.commit()
        db.close()
        cursor.close()
        return res
