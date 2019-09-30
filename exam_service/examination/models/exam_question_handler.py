from examination.dao.exam_question import create_exam_question, get_recent_exam_question,\
    get_exam_question_by_id, get_all_exam_question
from examination.views import exam_question as examquestionview


def post_handler(payload, cursor):
    exam_id = payload["examId"]
    question_id = payload["questionId"]
    total_marks = payload["totalMarks"]
    difficulty_level = payload["difficultyLevel"]
    create_exam_question(exam_id, question_id, total_marks, difficulty_level, cursor)
    res = get_recent_exam_question(cursor)
    return res


def get_handler(exam_question_id, cursor):
    if exam_question_id:
        exam_question = get_exam_question_by_id(exam_question_id, cursor)
        if exam_question:
            exam_question = examquestionview.single(exam_question)
        return exam_question
    exam_question = get_all_exam_question(cursor)
    if exam_question:
        exam_question = examquestionview.multiple(exam_question)
    return exam_question
