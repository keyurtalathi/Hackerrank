from userattempt.core.db_connections import connect_to_geecoder


def create_user_attempt(data,filepath):
    db, cursor = connect_to_geecoder()
    sql = "insert into user_attempt" \
          "(question_id,language_id,code_snippet)" \
          " values("+str(data["questionId"])+"," + data["languageId"] + ",'" +filepath+ "')"
    cursor.execute(sql)
    id = cursor.lastrowid
    cursor.close()
    db.close()
    return id

def update_user_attempt_by_id(user_attempt_id,data):
    db, cursor = connect_to_geecoder()
    sql = "update user_attempt set total_testcases_passed="+ str(data["noOfTestCasesPassed"])+", marks_obtained=" +\
          str(data["totalMarks"]) + " where id="+str(user_attempt_id)+")"
    cursor.execute(sql)
    cursor.close()
    db.close()
