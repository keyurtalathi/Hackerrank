from subprocess import Popen, PIPE
from questionanswer.dao.testcases import get_testcase_for_question

LANGUAGE_DICT = {
    "C": ".c",
    "PYTHON": ".py"
}


def write_to_file(code, language):
    file_path_input = "/home/geecoder/user_attempt/a" + LANGUAGE_DICT[language]
    fh = open(file_path_input, "w")
    fh.write(code)
    fh.close()
    return file_path_input


def run_c_code(file_path, question_id, data, cursor):
    gcc_output = Popen(["gcc", file_path, "-o", "run"], stdin=PIPE,
                       stdout=PIPE,
                       stderr=PIPE)
    output, error = gcc_output.communicate()
    if error:
        return {"error": error}
    testcases = get_testcase_for_question(cursor, question_id)
    data["testcases"] = []
    a_out_output = Popen(["./run"], stdin=PIPE, stdout=PIPE,
                         stderr=PIPE)
    input = open(testcases[0]["input"])
    input = input.read()
    output, error = a_out_output.communicate(input)
    output_file_pointer = open(testcases[0]["output"], "r")
    output_of_testcase = output_file_pointer.read()

    if output == output_of_testcase:
        return {"testcaseId": testcases[0]["id"], "isPassed": True}
    else:
        if output == output_of_testcase:
            return {"testcaseId": testcases[0]["id"], "isPassed": False}


def run_python_code(file_path, question_id, data, cursor):
    python_output = Popen(["python", file_path], stdin=PIPE,
                       stdout=PIPE,
                       stderr=PIPE)
    testcases = get_testcase_for_question(cursor, question_id)
    data["testcases"] = []
    input = open(testcases[0]["input"])
    input = input.read()
    output, error = python_output.communicate(input)
    output_file_pointer = open(testcases[0]["output"], "r")
    output_of_testcase = output_file_pointer.read()

    if output == output_of_testcase:
        return {"testcaseId": testcases[0]["id"], "isPassed": True}
    else:
        if output == output_of_testcase:
            return {"testcaseId": testcases[0]["id"], "isPassed": False}
