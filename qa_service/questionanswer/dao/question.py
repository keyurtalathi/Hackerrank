def get_question_by_id(question_id, cursor):
    sql = "SELECT * FROM question \
           WHERE id=" + str(question_id)

    cursor.execute(sql)
    result = cursor.fetchone()
    question_obj = {}
    if result:
        question_obj = {
            "id":result[0],
            "question": result[1],
            "description": result[2],
            "weightage":result[3],
            "difficulty_level": result[4],
            "question_type": result[5],
            "created_by": result[6],
            "created_on": result[7],
            "sub_topic_id": result[8]
        }

    return question_obj

def get_all_question(cursor):
    sql = "SELECT * FROM question"

    cursor.execute(sql)
    results = cursor.fetchall()
    questions_list = []
    for result in results:
        question_obj = {
            "id":result[0],
            "question": result[1],
            "description": result[2],
            "weightage":result[3],
            "difficulty_level": result[4],
            "question_type": result[5],
            "created_by": result[6],
            "created_on": result[7],
            "sub_topic_id": result[8]}
        questions_list.append(question_obj)

    return questions_list


def get_subtopicwise_question(sub_topic_id, cursor):
    sql = "SELECT * FROM question where sub_topic_id="+str(sub_topic_id)
    print sql
    cursor.execute(sql)
    results = cursor.fetchall()
    questions_list = []
    for result in results:
        question_obj = {
            "id": result[0],
            "question": result[1],
            "description": result[2],
            "weightage": result[3],
            "difficulty_level": result[4],
            "question_type": result[5],
            "created_by": result[6],
            "created_on": result[7],
            "sub_topic_id": result[8]}
        questions_list.append(question_obj)

    return questions_list

def add_question(question,description,weightage,difficulty_level,question_type,created_by,created_on,sub_topic_id,cursor):
    sql = "insert into question" \
          "(question," \
          "description," \
          "weightage," \
          "difficulty_level," \
          "question_type," \
          "created_by," \
          "created_on," \
          "sub_topic_id)" \
          " values('" +question+ "','',"+str(weightage)+",'"+difficulty_level+"','"+question_type+"',"+str(created_by)+","+str(created_on)+","+str(sub_topic_id)+")"
    cursor.execute(sql)

def get_recent_question(cursor):
    sql = "select * from question order by id  desc limit 1"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        return {
            "id":result[0],
            "question": result[1],
            "description": result[2],
            "weightage":result[3],
            "difficulty_level": result[4],
            "question_type": result[5],
            "created_by": result[6],
            "created_on": result[7],
            "sub_topic_id": result[8]
        }
    return {}


def update_question(ques_id, desc, cursor):
    sql = "update question set description='"+desc+"' where id="+str(ques_id)
    cursor.execute(sql)