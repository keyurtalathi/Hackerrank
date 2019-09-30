def single(exam_question_object):
    return {
        "id": exam_question_object["id"],
        "examId": exam_question_object["exam_id"],
        "questionId": exam_question_object["question_id"],
        "totalMarks": exam_question_object["total_marks"],
        "difficultyLevel": exam_question_object["difficulty_level"]
    }


def multiple(exam_question_objects):
    return [single(exam_question_object) for exam_question_object in exam_question_objects]
