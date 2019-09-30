from examination.dao.exam_attempt import create_exam_attempt, get_recent_exam_attempt,\
    get_exam_attempt_by_id, get_all_exam_attempt, update_exam_attempt
from examination.views import exam_attempt as examattemptview
from examination.core.exam_attempt_file_operation import write_code_snippet

def post_handler(payload, cursor):
    exam_question_id = payload["examQuestionId"]
    language_id = payload["languageId"]
    code_snippet = payload["codeSnippet"]
    total_testcases_passed = payload["totalTestcasesPassed"]
    marks_obtained = payload["marksObtained"]
    attempt_starttime = payload["timeStarted"]
    attempt_endtime = payload["timeEnded"]
    create_exam_attempt(exam_question_id, language_id, total_testcases_passed, code_snippet, marks_obtained \
                        , attempt_starttime, attempt_endtime, cursor)
    res = get_recent_exam_attempt(cursor)
    file_path = write_code_snippet(code_snippet, res["id"])
    update_exam_attempt(res["id"], file_path, cursor)
    res = get_recent_exam_attempt(cursor)
    return res


def get_handler(exam_attempt_id, cursor):
    if exam_attempt_id:
        exam_attempt = get_exam_attempt_by_id(exam_attempt_id, cursor)
        if exam_attempt:
            exam_attempt = examattemptview.single(exam_attempt)
        return exam_attempt
    exam_attempt = get_all_exam_attempt(cursor)
    if exam_attempt:
        exam_attempt = examattemptview.multiple(exam_attempt)
    return exam_attempt
