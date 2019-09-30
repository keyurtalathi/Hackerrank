
def single(testcase_object):
    return {
        "id": testcase_object["id"],
        "testcaseNumber":testcase_object["testcase_number"],
        "input":testcase_object["input"],
        "output":testcase_object["output"],
        "marks":testcase_object["marks"],
        "isExample":testcase_object["is_example"],
        "questionId":testcase_object["question_id"],
    }

def multiple(testcase_objects):
    print testcase_objects, "\n\n"
    return [single(testcase_object) for testcase_object in testcase_objects]