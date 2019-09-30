def single(exam_attempt_object):
    return {
        "id": exam_attempt_object["id"],
        "examQuestionId": exam_attempt_object["exam_question_id"],
        "languageId": exam_attempt_object["language_id"],
        "totalTestcasesPassed": exam_attempt_object["total_testcases_passed"],
        "codeSnippet": exam_attempt_object["code_snippet"],
        "marksObtained": exam_attempt_object["marks_obtained"],
        "timeStarted": exam_attempt_object["attempt_starttime"],
        "timeEnded": exam_attempt_object["attempt_endtime"]
    }


def multiple(exam_attempt_objects):
    return [single(exam_attempt_object) for exam_attempt_object in exam_attempt_objects]
