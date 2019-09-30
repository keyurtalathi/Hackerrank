from examination.controller.ping import Ping
from examination.controller.exam import Exam
from examination.controller.exam_question import ExamQuestion
from examination.controller.exam_attempt import ExamAttempt
from examination.controller.exam_testcase_result import ExamTestcaseResult


def router(api):
    api.add_resource(Ping, '/ping')
    api.add_resource(Exam, '/exam','/exam/<int:exam_id>')
    api.add_resource(ExamQuestion, '/examquestion','/examquestion/<int:exam_question_id>')
    api.add_resource(ExamAttempt, '/examattempt', '/examattempt/<int:exam_attempt_id>')
    api.add_resource(ExamTestcaseResult, '/examtestcaseresult', '/examtestcaseresult/<int:exam_testcase_id>')