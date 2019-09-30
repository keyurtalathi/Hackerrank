from questionanswer.dao.sub_topic import add_sub_topic,get_recent_sub_topic,get_sub_topic_id,get_all_sub_topic\
    ,get_topicwise_subtopic
from questionanswer.exceptions.unauthorised_exception import UnauthorisedException
from questionanswer.core.make_database_connection import connect_to_geecoder
from questionanswer.views import sub_topic as sub_topic_view


def get_handler(sub_topic_id,topic_id):
    db, cursor = connect_to_geecoder()
    if sub_topic_id:
        sub_topic= get_sub_topic_id(sub_topic_id, cursor)
        cursor.close()
        db.close()
        if sub_topic:
            sub_topic = sub_topic_view.single(sub_topic)
        return sub_topic
    elif topic_id:
        sub_topics = get_topicwise_subtopic(topic_id, cursor)
        cursor.close()
        db.close()
        if sub_topics:
            sub_topics = sub_topic_view.multiple(sub_topics)
            return sub_topics
    sub_topics = get_all_sub_topic(cursor)
    if sub_topics:
        sub_topics = sub_topic_view.multiple(sub_topics)
    cursor.close()
    db.close()
    return sub_topics

def post_handler(payload,user_context,cursor):

    if "teacher" in user_context["groups"]:
        topic_id = payload["topic_id"]
        sub_topic=payload["sub_topic"]
        add_sub_topic(sub_topic,topic_id,cursor)
        res = get_recent_sub_topic(cursor)
        return res

    else:
        raise UnauthorisedException
