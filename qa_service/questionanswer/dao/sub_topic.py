
def get_sub_topic_id(sub_topic_id, cursor):
    sql = "SELECT * FROM sub_topic \
           WHERE id=" + str(sub_topic_id)
    print sql

    cursor.execute(sql)
    result = cursor.fetchone()
    sub_topic_id_obj = {}
    if result:
        sub_topic_id_obj = {
            "id":result[0],
            "name": result[1],
            "topic_id": result[2]
        }

    return sub_topic_id_obj

def get_all_sub_topic(cursor):
    sql = "SELECT * FROM sub_topic"
    print sql

    cursor.execute(sql)
    results = cursor.fetchall()
    sub_topic_list = []
    for result in results:
        sub_topic_obj = {
            "id":result[0],
            "name": result[1],
            "topic_id": result[2]
        }
        sub_topic_list.append(sub_topic_obj)

    return sub_topic_list

def add_sub_topic(sub_topic,topic_id,cursor):
    sql = "insert into sub_topic(name,topic_id) values('" + sub_topic + "',"+str(topic_id)+")"
    cursor.execute(sql)

def get_recent_sub_topic(cursor):
    sql = "select * from sub_topic order by id  desc limit 1"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        return {
            "id": result[0],
            "name": result[1],
            "topic_id":result[2]
        }
    return {}


def get_topicwise_subtopic(topic_id, cursor):
    sql = "select * from sub_topic WHERE topic_id=" + str(topic_id)
    cursor.execute(sql)
    results = cursor.fetchall()
    sub_topic_list = []
    for result in results:
        sub_topic_obj = {
            "id": result[0],
            "name": result[1],
            "topic_id": result[2]
        }
        sub_topic_list.append(sub_topic_obj)

    return sub_topic_list