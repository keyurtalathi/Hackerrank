from os.path import dirname, abspath
from apigateway.utils.uniform_caching_interface import init_cache_handlers
from flask_cors import CORS
from redis import StrictRedis
from flask import Flask
from flask_restful import Api

# initialize DB connections

app = Flask(__name__)
app.root_dir = dirname(dirname(abspath(__file__)))
print("root dir", app.root_dir)
CORS(app)

# setup logger
from apigateway.conf.logger_setup import setup_config_logger

setup_config_logger(app)

# initialize cache handler
app.global_cache_handler = init_cache_handlers(app)
app.logger.info(app.global_cache_handler)
app.redis_client = StrictRedis()

# initializing the user apigateway interface for auth
from apigateway.conf.session_interfaces import UserServiceInterface

app.session_interface = UserServiceInterface()

# wrap app into flask restful extention

api = Api(app, prefix='/apigateway')

# set config

from apigateway.conf.config_setup import set_config

set_config(app)

# initialize boot-time variables
from apigateway.conf.init_startup_variables import init_variables

init_variables(app)

# initialize url mapping
from apigateway.controller.ping import Ping
from apigateway.controller.generic_controller import GenericHandler


api.add_resource(Ping, '/ping')
api.add_resource(GenericHandler, '/<resource_name>/<resource_id>/',
                 '/<resource_name>/')


if __name__ == '__main__':
    app.run(debug=True, port=4283)
