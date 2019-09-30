
def single(topic_object):
    return {
        "id": topic_object["id"],
        "topic": topic_object["name"],
    }

def multiple(topic_objects):
    print topic_objects, "\n\n"
    return [single(topic_object) for topic_object in topic_objects]