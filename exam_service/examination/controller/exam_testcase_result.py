from flask import request,current_app as app
from examination.conf.resource import BaseResource
from examination.models.exam_testcase_result_handler import post_handler,get_handler
from examination.core.make_database_connection import connect_to_geecoder
from examination.views import exam_testcase_result as examtestcaseresultview


class ExamTestcaseResult(BaseResource):
    def get(self, exam_testcase_id=None):
        app.logger.info("in examatestcaseresult get")
        db, cursor = connect_to_geecoder()
        res = get_handler(exam_testcase_id,cursor)
        db.commit()
        db.close()
        cursor.close()
        return res

    def post(self):
        app.logger.info("in examatestcaseresult post")
        payload = request.json
        db, cursor = connect_to_geecoder()
        res = post_handler(payload,cursor)
        if res:
            res = examtestcaseresultview.single(res)
        db.commit()
        db.close()
        cursor.close()
        return res
