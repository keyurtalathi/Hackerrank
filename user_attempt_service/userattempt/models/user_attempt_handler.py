from userattempt.core.write_to_file import write_to_file
from userattempt.core.run_code import run_c_code, run_python_code
from userattempt.dao.user_attempt import create_user_attempt, \
    update_user_attempt_by_id


def handle_and_run_code(data, write_message):
    file_path = write_to_file(data["codeSnippet"], data["username"],
                              data["questionId"], data["language"])
    user_attempt_id = create_user_attempt(data, file_path)
    data["userAttemptId"] = user_attempt_id
    if data["language"] == "C":
        data = run_c_code(file_path, data["questionId"], write_message, data)
        update_user_attempt_by_id(user_attempt_id, data)
    elif data["language"] == "PYTHON":
        data = run_python_code(file_path, data["questionId"], write_message, data)
        update_user_attempt_by_id(user_attempt_id, data)
