import os
from examination.conf.environment import get_config_module
from importlib import import_module


def get_env_config():
    geecoder_env = os.environ.get('GEECODER_ENV', 'dev')
    module_path = get_config_module(geecoder_env)
    config_module = import_module(module_path)
    config = getattr(config_module, 'Config')
    return config
