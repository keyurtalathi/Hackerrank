from questionanswer.dao.question import add_question, get_recent_question, get_question_by_id, \
    get_all_question, update_question, get_subtopicwise_question
from questionanswer.exceptions.unauthorised_exception import UnauthorisedException
from questionanswer.core.make_database_connection import connect_to_geecoder
from questionanswer.views import question as question_view
from questionanswer.core.desc_file_operation import write_desc


def get_handler(question_id, sub_topic_id):
    db, cursor = connect_to_geecoder()
    if question_id:
        question = get_question_by_id(question_id, cursor)
        cursor.close()
        db.close()
        if question:
            question = question_view.single(question)
        return question
    elif sub_topic_id:
        questions = get_subtopicwise_question(sub_topic_id, cursor)
        if questions:
            questions = question_view.multiple(questions)
        cursor.close()
        db.close()
        return questions
    questions = get_all_question(cursor)
    if questions:
        questions = question_view.multiple(questions)
    cursor.close()
    db.close()
    return questions


def post_handler(payload, user_context, cursor):
    if "teacher" in user_context["groups"]:
        question = payload["question"]
        description = payload["description"]
        weightage = payload["weightage"]
        difficulty_level = payload["difficultyLevel"]
        question_type = payload["questionType"]
        created_by = payload["createdBy"]
        created_on = payload["createdOn"]
        sub_topic_id = payload["subTopic"]
        add_question(question, description, weightage, difficulty_level, question_type, created_by, created_on,
                     sub_topic_id, cursor)
        res = get_recent_question(cursor)
        file_path = write_desc(description,res["id"])
        update_question(res["id"],file_path,cursor)
        res = get_recent_question(cursor)
        return res
    else:
        raise UnauthorisedException
