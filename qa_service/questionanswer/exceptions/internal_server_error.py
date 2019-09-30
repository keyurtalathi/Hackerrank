from questionanswer.conf.error_object import ErrorObject


class InternalServerError(Exception):
    """Raise when something goes wrong"""

    def __init__(self, errorObject=None):
        if errorObject:
            self.errorObject = errorObject
        else:
            self.errorObject = ErrorObject(errorCode=500,
                                           errorMessage='Internal server error')

    def __str__(self):
        return str(self.errorObject.errorMessage)
