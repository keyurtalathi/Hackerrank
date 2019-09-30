from questionanswer.core.run_codes import write_to_file,run_c_code,run_python_code


def post_handler(payload, cursor):
    file_path = write_to_file(payload["codeSnippet"],payload["language"])
    res={}
    if payload["language"]=="C":
        res = run_c_code(file_path,payload["questiionId"],payload,cursor)
    elif payload["language"]=="PYTHON":
        res = run_python_code(file_path,payload["questiionId"],payload,cursor)
    return res
