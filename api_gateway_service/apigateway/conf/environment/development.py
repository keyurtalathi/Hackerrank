from apigateway.conf.environment.base import BaseConfig
from datetime import datetime


class Config(BaseConfig):
    USER_SERVICE_URL = "http://127.0.0.1:8737"
    DOWNLOAD_ROOT = "/var/www/"
    DOWNLOAD_URL_ROOT = "http://0.0.0.0/downloads/"
    QA_SERVICE_URL = "http://127.0.0.1:7837"
    # KAFKA_URL = ["35.185.128.206", "107.167.178.227"]
    # KAFKA_PORT = "9092"
    # KAFKA_CONSUMER_GROUP = 'local'