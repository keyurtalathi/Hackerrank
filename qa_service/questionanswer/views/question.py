
def single(question_object):
    return {
        "id": question_object["id"],
        "question":question_object["question"],
        "description":question_object["description"],
        "weightage":question_object["weightage"],
        "difficultyLevel":question_object["difficulty_level"],
        "questionType":question_object["question_type"],
        "createdBy":question_object["created_by"],
        "createdOn":question_object["created_on"],
        "subTopicId":question_object["sub_topic_id"]
    }

def multiple(question_objects):
    print question_objects, "\n\n"
    return [single(question_object) for question_object in question_objects]