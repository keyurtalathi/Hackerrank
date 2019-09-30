def single(exam_testcase_result_object):
    return {
        "id": exam_testcase_result_object["id"],
        "examAttemptId": exam_testcase_result_object["exam_attempt_id"],
        "testcaseId": exam_testcase_result_object["testcase_id"],
        "isPassed": exam_testcase_result_object["is_passed"]
    }


def multiple(exam_testcase_result_objects):
    return [single(exam_testcase_result_object) for exam_testcase_result_object in exam_testcase_result_objects]
