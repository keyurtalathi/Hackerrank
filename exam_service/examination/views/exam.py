
def single(exam_object):
    return {
        "id": exam_object["id"],
        "examName": exam_object["name"],
        "startTime": exam_object["starttime"],
        "endTime": exam_object["endtime"]
    }

def multiple(exam_objects):
    return [single(exam_object) for exam_object in exam_objects]