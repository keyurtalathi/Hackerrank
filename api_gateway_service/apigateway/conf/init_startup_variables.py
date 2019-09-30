from apigateway.utils.config_utils import get_env_config

def init_variables(app):
    if not app:
        raise Exception
    app.auth_header_name = 'X-Authorization-Token'
    config = get_env_config()

    return
