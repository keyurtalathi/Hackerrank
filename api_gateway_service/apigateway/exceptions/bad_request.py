from apigateway.conf.error_object import ErrorObject


class BadRequest(Exception):
    def __init__(self, message="Bad request"):
        self.errorObject = ErrorObject(errorMessage=message, errorCode=400)

    def _serialize(self):
        return self.errorObject.errorMessage
