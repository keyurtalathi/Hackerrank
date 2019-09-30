from examination.dao.exam import create_exam, get_recent_exam, get_all_exam, get_exam_by_id
from examination.views import exam as examview


def post_handler(payload, cursor):
    exam_name = payload["examName"]
    start_time = payload["startTime"]
    end_time = payload["endTime"]
    create_exam(exam_name, start_time, end_time, cursor)
    res = get_recent_exam(cursor)
    return res


def get_handler(exam_id, cursor):
    if exam_id:
        exam = get_exam_by_id(exam_id, cursor)
        if exam:
            exam = examview.single(exam)
        return exam
    exam = get_all_exam(cursor)
    if exam:
        exam = examview.multiple(exam)
    return exam
