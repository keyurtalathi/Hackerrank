from apigateway.conf.error_object import ErrorObject

class UnauthorisedException(Exception):
	def __init__(self,message="Authorization Failure"):
		self.errorObject = ErrorObject(errorMessage=message,errorCode=401)

	def _serialize(self):
		return self.errorObject.errorMessage