from userattempt.core.kafka_consumer import Worker
import json
from userattempt.core.db_connections import connect_to_geecoder

def insert_testcases(testcase):
    testcase = json.loads(testcase)
    db, cursor = connect_to_geecoder()
    sql = "insert into testcase_result(testcase_id, user_attempt_id, is_passed) values("+\
          testcase["testcaseId"]+","+testcase["userAttemptId"]+","+testcase["isPassed"]+")"
    cursor.execute(sql)

if __name__ == '__main__':
    url = "localhost"
    ticket_worker = Worker(
        topic='testcase',
        url=url, client_id="local")
    print "testcase consumer started"
    while (True):
        ticket_worker.compute(insert_testcases)
