from questionanswer.dao.testcase import get_testcase_by_id,get_testcases_by_question_id,add_testcase,get_recent_testcase,update_testcase
from questionanswer.exceptions.unauthorised_exception import UnauthorisedException
from questionanswer.core.make_database_connection import connect_to_geecoder
from questionanswer.views import testcase as testcase_view
from questionanswer.core.testcase_file_operation import write_testcase_input,write_testcase_output

def get_handler(params):
    db, cursor = connect_to_geecoder()
    if params.get("question_id"):
        testcases = get_testcases_by_question_id(params["question_id"], cursor)
        cursor.close()
        db.close()
        if testcases:
            testcases = testcase_view.multiple(testcases)
        return testcases
    testcase = get_testcase_by_id(params["testcase_id"], cursor)
    db.close()
    cursor.close()
    if testcase:
        testcase = testcase_view.single(testcase)
    return testcase


def post_handler(payload, user_context, cursor):
    if "teacher" in user_context["groups"]:
        testcase_number = payload["testcaseNumber"]
        input = payload["input"]
        output = payload["output"]
        marks= payload["marks"]
        is_example= payload["isExample"]
        question_id = payload["questionId"]
        add_testcase(testcase_number,marks,is_example,question_id,cursor)
        res = get_recent_testcase(cursor)
        file_path_input= write_testcase_input(input,res["id"])
        file_path_output = write_testcase_output(output,res["id"])
        update_testcase(res["id"],file_path_input,file_path_output,cursor)
        res = get_recent_testcase(cursor)
        return res
    else:
        raise UnauthorisedException
