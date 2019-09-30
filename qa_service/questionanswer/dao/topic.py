
def get_topic_id(topic_id, cursor):
    sql = "SELECT * FROM topic \
           WHERE id=" + str(topic_id)
    print sql

    cursor.execute(sql)
    result = cursor.fetchone()
    topic_id_obj = {}
    if result:
        topic_id_obj = {
            "id":result[0],
            "name": result[1],
        }

    return topic_id_obj


def get_all_sub_topic(cursor):
    sql = "SELECT * FROM topic"
    print sql

    cursor.execute(sql)
    results = cursor.fetchall()
    topic_list = []
    for result in results:
        topic_obj = {
            "id":result[0],
            "name": result[1],
        }
        topic_list.append(topic_obj)

    return topic_list


def add_topic(topic,cursor):
    sql = "insert into topic(name) values('" + topic + "')"
    cursor.execute(sql)


def get_recent_topic(cursor):
    sql = "select * from topic order by id  desc limit 1"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        return {
            "id": result[0],
            "name": result[1]
        }
    return {}