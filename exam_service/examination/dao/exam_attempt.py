def create_exam_attempt(exam_question_id, language_id, total_testcases_passed, code_snippet, marks_obtained, \
                        attempt_starttime, attempt_endtime, cursor):
    sql = "insert into exam_attempt(exam_question_id, language_id, total_testcases_passed, code_snippet \
    , marks_obtained, attempt_starttime, attempt_endtime) values(" + str(exam_question_id) + \
          "," + str(language_id) + \
          "," + str(total_testcases_passed) + \
          ",'" + code_snippet + \
          "'," + str(marks_obtained) + \
          "," + str(attempt_starttime) + \
          "," + str(attempt_endtime) + ")"
    cursor.execute(sql)


def update_exam_attempt(exam_attempt_id, code_snippet, cursor):
    sql = "update exam_attempt set code_snippet = '"+ code_snippet + "' where id = " +str(exam_attempt_id)
    cursor.execute(sql);


def get_recent_exam_attempt(cursor):
    sql = "select * from exam_attempt order by id  desc limit 1"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        return {
            "id": result[0],
            "exam_question_id": result[1],
            "language_id": result[2],
            "total_testcases_passed": result[3],
            "code_snippet": result[4],
            "marks_obtained": result[5],
            "attempt_starttime": result[6],
            "attempt_endtime": result[7]
        }
    return {}


def get_exam_attempt_by_id(exam_attempt_id, cursor):
    sql = "SELECT * FROM exam_attempt WHERE id=" + str(exam_attempt_id)
    cursor.execute(sql)
    result = cursor.fetchone()

    if result:
        return {
            "id": result[0],
            "exam_question_id": result[1],
            "language_id": result[2],
            "total_testcases_passed": result[3],
            "code_snippet": result[4],
            "marks_obtained": result[5],
            "attempt_starttime": result[6],
            "attempt_endtime": result[7]
        }
    return {}


def get_all_exam_attempt(cursor):
    sql = "SELECT * FROM exam_attempt"
    cursor.execute(sql)
    exam_attempt_obj = []
    results = cursor.fetchall()
    for result in results:
        exam_attempt_obj.append({
            "id": result[0],
            "exam_question_id": result[1],
            "language_id": result[2],
            "total_testcases_passed": result[3],
            "code_snippet": result[4],
            "marks_obtained": result[5],
            "attempt_starttime": result[6],
            "attempt_endtime": result[7]
        })
    return exam_attempt_obj
