from os.path import dirname, abspath
from flask import Flask
from flask_cors import CORS
from userauthentication.controller.ping import Ping
from userauthentication.controller.user import User
from userauthentication.controller.validation import UserValidation
from userauthentication.conf.logger_setup import setup_config_logger
from flask_restful import Api
from userauthentication.conf.config_setup import set_config

# initialize DB connectionsgit@gitlab.com:15102_15153_15228/se18.git

app = Flask(__name__)
app.root_dir = dirname(dirname(abspath(__file__)))
CORS(app)
# setup logger
setup_config_logger(app)
# wrap app into flask restful extention
api = Api(app, prefix='/userservice')
# set config
set_config(app)
# initialize url mapping
api.add_resource(Ping, '/ping')
api.add_resource(User, '/user',
                 '/user/<string:user_id>')
api.add_resource(UserValidation, '/uservalidation')

if __name__ == '__main__':
    app.run(debug=True, port=8737)
