from questionanswer.dao.topic import add_topic,get_recent_topic,get_topic_id,get_all_sub_topic
from questionanswer.exceptions.unauthorised_exception import UnauthorisedException
from questionanswer.core.make_database_connection import connect_to_geecoder
from questionanswer.views import topic as topic_view


def get_handler(topic_id):
    db, cursor = connect_to_geecoder()
    if topic_id:
        topic= get_topic_id(topic_id, cursor)
        cursor.close()
        db.close()
        if topic:
            topic = topic_view.single(topic)
        return topic
    topics = get_all_sub_topic(cursor)
    if topics:
        topics = topic_view.multiple(topics)
    cursor.close()
    db.close()
    return topics

def post_handler(payload,user_context,cursor):

    if "teacher" in user_context["groups"]:
        topic = payload["topic"]
        add_topic(topic,cursor)
        res = get_recent_topic(cursor)
        return res

    else:
        raise UnauthorisedException
