from os.path import dirname, abspath
from examination.utils.uniform_caching_interface import init_cache_handlers
from flask_cors import CORS
from redis import StrictRedis
from flask import Flask
from flask_restful import Api
from examination.conf.router import router

# initialize DB connections

app = Flask(__name__)
app.root_dir = dirname(dirname(abspath(__file__)))
print("root dir", app.root_dir)
CORS(app)

# setup logger
from examination.conf.logger_setup import setup_config_logger

setup_config_logger(app)

# initialize cache handler
app.global_cache_handler = init_cache_handlers(app)
app.logger.info(app.global_cache_handler)
app.redis_client = StrictRedis()

# wrap app into flask restful extention

api = Api(app, prefix='/examination')

# set config

from examination.conf.config_setup import set_config

set_config(app)

# initialize boot-time variables
from examination.conf.init_startup_variables import init_variables

init_variables(app)

# initialize url mapping


router(api)

if __name__ == '__main__':
    app.run(debug=True, port=3926)
