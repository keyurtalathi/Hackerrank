def create_exam_question(exam_id, question_id, total_marks, difficulty_level, cursor):
    sql = "insert into exam_question(exam_id, question_id, total_marks, difficulty_level) values(" + str(exam_id)+ \
          "," + str(question_id) + \
          "," + str(total_marks) + \
          ",'" + difficulty_level + "')"
    cursor.execute(sql)


def get_recent_exam_question(cursor):
    sql = "select * from exam_question order by id  desc limit 1"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        return {
            "id": result[0],
            "exam_id": result[1],
            "question_id": result[2],
            "total_marks": result[3],
            "difficulty_level": result[4]
        }
    return {}


def get_exam_question_by_id(exam_question_id, cursor):
    sql = "SELECT * FROM exam_question WHERE id=" + str(exam_question_id)
    cursor.execute(sql)
    result = cursor.fetchone()

    if result:
        return {
            "id": result[0],
            "exam_id": result[1],
            "question_id": result[2],
            "total_marks": result[3],
            "difficulty_level": result[4]
        }
    return {}


def get_all_exam_question(cursor):
    sql = "SELECT * FROM exam_question"
    cursor.execute(sql)
    exam_obj = []
    results = cursor.fetchall()
    for result in results:
        exam_obj.append({
            "id": result[0],
            "exam_id": result[1],
            "question_id": result[2],
            "total_marks": result[3],
            "difficulty_level": result[4]
        })
    return exam_obj
