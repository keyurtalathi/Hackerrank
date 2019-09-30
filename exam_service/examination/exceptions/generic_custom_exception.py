from examination.conf.error_object import ErrorObject


class GenericCustomException(Exception):
    def __init__(self, msg='Something went Wrong', code=400):
        error_object = ErrorObject()
        error_object.errorCode = code
        error_object.errorMessage = msg
        self.errorObject = error_object

    def __str__(self):
        return str(self.errorObject.errorMessage)
