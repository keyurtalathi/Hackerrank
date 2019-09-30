import os
import logging


log_format = ' '.join([
    '[%(asctime)s]',
    '[%(process)d-%(thread)d]',
    '%(levelname)s',
    '-',
    '%(message)s'
])

formatter = logging.Formatter(log_format)


def setup_config_logger(app):

    # TODO: Generated by python uuid.uuid4. Get a better key later on
    app.debug_log_format = log_format

    if not app.debug:
        logHandler = logging.StreamHandler()
        logHandler.setFormatter(formatter)
        logHandler.setLevel(logging.DEBUG)
        app.logger.addHandler(logHandler)
        app.logger.setLevel(logging.DEBUG)