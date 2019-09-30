CONFIG_MAP = {
    'prod': 'production',
    'staging': 'staging',
    'dev': 'development',
    'local': 'local'
}


def get_config(env):
    return '.'.join(['examination', 'conf', 'environment',
                     CONFIG_MAP.get(env, env), 'Config'])


def get_config_module(env):
    return '.'.join(['examination', 'conf', 'environment',
                     CONFIG_MAP.get(env, env)])
