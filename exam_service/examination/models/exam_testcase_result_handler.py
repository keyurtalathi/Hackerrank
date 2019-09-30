from examination.dao.exam_testcase_result import create_exam_testcase_result,get_recent_exam_testcase_result \
    ,get_exam_testcase_result_by_id,get_all_exam_testcase_result
from examination.views import exam_testcase_result as examtestcaseresultview


def post_handler(payload, cursor):
    exam_attempt_id = payload["examAttemptId"]
    testcase_id = payload["testcaseId"]
    is_passed = payload["isPassed"]
    create_exam_testcase_result(exam_attempt_id, testcase_id, is_passed, cursor)
    res = get_recent_exam_testcase_result(cursor)
    return res


def get_handler(exam_testcase_result_id, cursor):
    if exam_testcase_result_id:
        exam_testcase_result = get_exam_testcase_result_by_id(exam_testcase_result_id, cursor)
        if exam_testcase_result:
            exam_testcase_result = examtestcaseresultview.single(exam_testcase_result)
        return exam_testcase_result
    exam_testcase_result = get_all_exam_testcase_result(cursor)
    if exam_testcase_result:
        exam_testcase_result = examtestcaseresultview.multiple(exam_testcase_result)
    return exam_testcase_result
