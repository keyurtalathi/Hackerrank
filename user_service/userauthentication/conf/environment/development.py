from userauthentication.conf.environment.base import BaseConfig
from datetime import datetime


class Config(BaseConfig):
    USER_DB_URL = "127.0.0.1"
    USER_DB_USER = "root"
    USER_DB_PASSWORD = "as2d2p"
    USER_DATABASE = "user_database"
