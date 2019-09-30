from questionanswer.utils.config_utils import get_env_config


def write_desc(description,question_id):
    config = get_env_config()
    file_path = config.DESCRIPTION_FILE_PATH+str(question_id)
    fh = open(file_path, "w")
    fh.write(description)
    fh.close()
    return file_path