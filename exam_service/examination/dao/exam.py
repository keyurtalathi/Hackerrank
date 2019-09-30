def create_exam(exam_name, start_time, duration, cursor):
    sql = "insert into exam(name,starttime,endtime) values('" + exam_name + \
          "'," + str(start_time) + \
          "," + str(duration) + ")"
    cursor.execute(sql)


def get_recent_exam(cursor):
    sql = "select * from exam order by id  desc limit 1"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        return {
            "id": result[0],
            "name": result[1],
            "starttime": result[2],
            "endtime": result[3]
        }
    return {}


def get_exam_by_id(exam_id, cursor):
    sql = "SELECT * FROM exam WHERE id=" + str(exam_id)
    cursor.execute(sql)
    result = cursor.fetchone()

    if result:
        return {
            "id": result[0],
            "name": result[1],
            "starttime": result[2],
            "endtime": result[3]
        }
    return {}


def get_all_exam(cursor):
    sql = "SELECT * FROM exam"
    cursor.execute(sql)
    exam_obj = []
    results = cursor.fetchall()
    for result in results:
        exam_obj.append({
            "id": result[0],
            "name": result[1],
            "starttime": result[2],
            "endtime": result[3]
        })
    return exam_obj
