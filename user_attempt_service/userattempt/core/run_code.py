import sys
import json
import pexpect
from subprocess import Popen, PIPE
from userattempt.core.db_connections import connect_to_geecoder
from userattempt.dao.testcases import get_testcase_for_question
from userattempt.core.kafka_producer import MessageQueue


def run_c_code(file_path, question_id, write_message, data):
    gcc_output = Popen(["gcc", file_path, "-o", "run"], stdin=PIPE, stdout=PIPE,
                       stderr=PIPE)
    output, error = gcc_output.communicate()
    queue = MessageQueue()
    if error:
        write_message(str(error))
    else:
        db, cursor = connect_to_geecoder()
        testcases = get_testcase_for_question(cursor, question_id)
        data["testcases"] = []
        no_of_testcases_passed = 0
        total_marks = 0
        for testcase in testcases:
            a_out_output = Popen(["./run"], stdin=PIPE, stdout=PIPE,
                                 stderr=PIPE)
            input = open(testcase["input"])
            input_test = input.read()
            output, error = a_out_output.communicate(input_test)
            output_file_pointer = open(testcase["output"], "r")
            output_of_testcase = output_file_pointer.read()
            if output == output_of_testcase:
                write_message(json.dumps({str(testcase[id]): True}))
                data["testcaseId"]= testcase["id"]
                data["isPassed"]= True
                queue.queue(topic='testcase', msg=json.dumps(data))
                no_of_testcases_passed = no_of_testcases_passed + 1
                total_marks = total_marks + testcase["marks"]
            else:
                write_message(json.dumps({str(testcase[id]): False}))
                data["testcaseId"] = testcase["id"]
                data["isPassed"] = False
                queue.queue(topic='testcase', msg=json.dumps(data))
        data["noOfTestCasesPassed"] = no_of_testcases_passed
        data["totalMarks"] = total_marks
        db.close()
        cursor.close()
        return data


def run_python_code(file_path, question_id, write_message, data):
    queue = MessageQueue()
    db, cursor = connect_to_geecoder()
    testcases = get_testcase_for_question(cursor, question_id)
    data["testcases"] = []
    no_of_testcases_passed = 0
    total_marks = 0
    for testcase in testcases:
        input_test = open(testcase["input"])
        input_testcase = input_test.read()

        a_out_output = Popen(["python", file_path], stdin=PIPE, stdout=PIPE,
                             stderr=PIPE)
        output, error = a_out_output.communicate(input_testcase)
        if error:
            write_message(json.dumps({"error":error}))
        else:
            output_file_pointer = open(testcase["output"], "r")
            output_of_testcase = output_file_pointer.read()
            if output == output_of_testcase:
                write_message(json.dumps({str(testcase[id]): True}))
                data["testcaseId"]=testcase["id"]
                data["isPassed"]=True
                queue.queue(topic='testcase', msg=json.dumps(data))
                no_of_testcases_passed = no_of_testcases_passed + 1
                total_marks = total_marks + testcase["marks"]
            else:
                write_message(json.dumps({str(testcase[id]): False}))
                data["testcaseId"] = testcase["id"]
                data["isPassed"] = False
                queue.queue(topic='testcase', msg=json.dumps(data))
    data["noOfTestCasesPassed"] = no_of_testcases_passed
    data["totalMarks"] = total_marks
    db.close()
    cursor.close()
    return data
