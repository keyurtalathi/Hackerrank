def create_exam_testcase_result(exam_attempt_id, testcase_id, is_passed, cursor):
    sql = "insert into exam_testcase_result(exam_attempt_id, testcase_id, is_passed) values(" + str(exam_attempt_id) + \
          "," + str(testcase_id) + \
          "," + str(is_passed) + ")"
    cursor.execute(sql)


def get_recent_exam_testcase_result(cursor):
    sql = "select * from exam_testcase_result order by id  desc limit 1"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        return {
            "id": result[0],
            "exam_attempt_id": result[1],
            "testcase_id": result[2],
            "is_passed": result[3]
        }
    return {}


def get_exam_testcase_result_by_id(exam_testcase_result_id, cursor):
    sql = "SELECT * FROM exam_testcase_result WHERE id=" + str(exam_testcase_result_id)
    cursor.execute(sql)
    result = cursor.fetchone()

    if result:
        return {
            "id": result[0],
            "exam_attempt_id": result[1],
            "testcase_id": result[2],
            "is_passed": result[3]
        }
    return {}


def get_all_exam_testcase_result(cursor):
    sql = "SELECT * FROM exam_testcase_result"
    cursor.execute(sql)
    exam_testcase_result_obj = []
    results = cursor.fetchall()
    for result in results:
        exam_testcase_result_obj.append({
            "id": result[0],
            "exam_attempt_id": result[1],
            "testcase_id": result[2],
            "is_passed": result[3]
        })
    return exam_testcase_result_obj
