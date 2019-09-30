def get_testcase_for_question(cursor, question_id):
    sql = "select * from testcase where question_id=" + question_id
    cursor.execute(sql)
    results = cursor.fetchall()
    testcases_list = []
    for result in results:
        testcases_list.append({
            "id": result[0],
            "testcase_number": result[1],
            "input": result[2],
            "output": result[3],
            "marks": result[4],
            "is_example": result[5],
            "question_id": result[6]
        })
    return []