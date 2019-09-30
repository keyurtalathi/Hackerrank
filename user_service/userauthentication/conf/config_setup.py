from userauthentication.conf.environment import get_config
import os


def set_config(app):
    app.secret_key = "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"
    geecoder_env = os.environ.get('GEECODER_ENV', 'dev')
    config = get_config(geecoder_env)
    app.config.from_object(config)
    return
