from questionanswer.controller.ping import Ping
from questionanswer.controller.topic import Topic
from questionanswer.controller.sub_topic import SubTopic
from questionanswer.controller.question import Question
from questionanswer.controller.testcase import Testcase
from questionanswer.controller.language import Language
from questionanswer.controller.run_program import Run


def router(api):
    api.add_resource(Ping, '/ping')
    api.add_resource(Topic, '/topic')
    api.add_resource(SubTopic, '/subtopic')
    api.add_resource(Question, '/question')
    api.add_resource(Testcase,'/testcase')
    api.add_resource(Language, '/language')
    api.add_resource(Run,'/run')
