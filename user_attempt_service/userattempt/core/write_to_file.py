from datetime import datetime

LANGUAGE_DICT = {
    "C":".c",
    "PYTHON":".py"
}

def write_to_file(code, username, questionId, language):
    time = datetime.now()
    file_path_input = "/home/geecoder/user_attempt/"+username+"/"+str(questionId)+str(time)+LANGUAGE_DICT[language]
    fh = open(file_path_input, "w")
    fh.write(code)
    fh.close()
    return file_path_input
