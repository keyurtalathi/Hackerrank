

def single(sub_topic_object):
    return {
        "id": sub_topic_object["id"],
        "subTopic":sub_topic_object["name"],
        "topicId":sub_topic_object["topic_id"]
    }

def multiple(sub_topic_objects):
    print sub_topic_objects, "\n\n"
    return [single(sub_topic_object) for sub_topic_object in sub_topic_objects]