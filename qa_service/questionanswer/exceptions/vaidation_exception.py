from questionanswer.conf.error_object import ErrorObject


class ValidationException(Exception):
    """Raise when something goes wrong in the request validation"""

    def __init__(self, errorMessage="Validation failure", errorCode=400):
        self.errorObject = ErrorObject(errorMessage=errorMessage, errorCode=errorCode)

    def __str__(self):
        return str(self.errorObject.errorMessage)


if __name__ == "__main__":
    from questionanswer.conf.error_object import ErrorObject

    try:
        raise ValidationException(ErrorObject(errorCode=400, errorMessage="validation exception!!"))
    except ValidationException as exc:
        print exc
