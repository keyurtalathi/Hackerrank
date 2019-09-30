from examination.utils.config_utils import get_env_config


def write_code_snippet(code_snippet,exam_attempt_id):
    config = get_env_config()
    file_path = config.EXAM_ATTEMPT_FILE_PATH+str(exam_attempt_id)
    fh = open(file_path, "w")
    fh.write(code_snippet)
    fh.close()
    return file_path