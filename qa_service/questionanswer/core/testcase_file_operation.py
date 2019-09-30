from questionanswer.utils.config_utils import get_env_config


def write_testcase_input(input,testcase_id):
    config = get_env_config()
    file_path_input = config.TESTCASE_FILE_PATH_INPUT+str(testcase_id)
    fh = open(file_path_input, "w")
    fh.write(input)
    fh.close()
    return file_path_input

def write_testcase_output(output,testcase_id):
    config = get_env_config()
    file_path_output = config.TESTCASE_FILE_PATH_OUTPUT+str(testcase_id)
    fh = open(file_path_output, "w")
    fh.write(output)
    fh.close()
    return file_path_output