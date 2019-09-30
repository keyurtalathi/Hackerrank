CONFIG_MAP = {
    'prod': 'production',
    'staging': 'staging',
    'dev': 'development',
}


def get_config(env):
    return '.'.join(['userauthentication', 'conf', 'environment',
                     CONFIG_MAP.get(env, env), 'Config'])


def get_config_module(env):
    return '.'.join(['userauthentication', 'conf', 'environment',
                     CONFIG_MAP.get(env, env)])
