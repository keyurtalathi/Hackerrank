from questionanswer.conf.environment.base import BaseConfig
from datetime import datetime

class Config(BaseConfig):
    GEECODER_DB_URL = "127.0.0.1"
    GEECODER_DB_USER = "root"
    GEECODER_DB_PASSWORD = "teju@123"
    GEECODER_DATABASE = "geecoder_database"
    DESCRIPTION_FILE_PATH = "/home/geecoder/description/"
    TESTCASE_FILE_PATH_INPUT="/home/geecoder/testcase/input/"
    TESTCASE_FILE_PATH_OUTPUT = "/home/geecoder/testcase/output/"

    # KAFKA_URL = ["35.185.128.206", "107.167.178.227"]
    # KAFKA_PORT = "9092"
    # KAFKA_CONSUMER_GROUP = 'local'