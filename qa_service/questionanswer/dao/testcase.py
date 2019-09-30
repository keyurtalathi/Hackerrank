
def get_testcase_by_id(testcase_id, cursor):
    sql = "SELECT * FROM testcase \
           WHERE id=" + str(testcase_id)
    print sql

    cursor.execute(sql)
    result = cursor.fetchone()
    testcase_obj = {}
    if result:
        testcase_obj = {
            "id":result[0],
            "testcase_number": result[1],
            "input": result[2],
            "output":result[3],
            "marks": result[4],
            "is_example": result[5],
            "question_id": result[6]
        }

    return testcase_obj

def get_testcases_by_question_id(question_id, cursor):
    sql = "SELECT * FROM testcase \
           WHERE question_id=" + str(question_id)
    print sql

    cursor.execute(sql)
    results = cursor.fetchall()
    testcases_list = []
    for result in results:
        testcase_obj = {
            "id": result[0],
            "testcase_number": result[1],
            "input": result[2],
            "output": result[3],
            "marks": result[4],
            "is_example": result[5],
            "question_id": result[6]
        }
        testcases_list.append(testcase_obj)

    return testcases_list


def add_testcase(testcase_number,marks,isexample,question_id,cursor):
    sql = "insert into testcase" \
          "(testcase_number," \
          "input," \
          "ouput," \
          "marks," \
          "is_example," \
          "question_id)" \
          " values("+str(testcase_number)+",'','',"+str(marks)+","+str(isexample)+","+str(question_id)+")"
    cursor.execute(sql)

def get_recent_testcase(cursor):
    sql = "select * from testcase order by id  desc limit 1"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        return {
            "id":result[0],
            "testcase_number": result[1],
            "input": result[2],
            "output":result[3],
            "marks": result[4],
            "is_example": result[5],
            "question_id": result[6]
        }
    return {}

def update_testcase(testcase_id,input,output,cursor):
    sql = "update testcase set input='"+input+"',ouput='"+output+"' where id="+str(testcase_id)
    cursor.execute(sql)